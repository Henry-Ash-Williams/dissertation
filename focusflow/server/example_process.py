#!/usr/bin/env python3 

import numpy as np 
import dlib 
import cv2 
import torch 
import sys 
import os 

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('./shape_predictor_68_face_landmarks.dat')

class FaceNotFoundException(Exception):
    def __init__(self, message="Could not find a face in this image"):
        self.message = message 
        super().__init__(self.message)

def process_frame(frame: np.ndarray) -> dict:
    def get_eye_bbox(points): 
        max_lep_x = max(points, key=lambda point: point.x).x
        max_lep_y = max(points, key=lambda point: point.y).y
        min_lep_x = min(points, key=lambda point: point.x).x
        min_lep_y = min(points, key=lambda point: point.y).y

        return max_lep_x, max_lep_y, min_lep_x, min_lep_y

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    grid = np.zeros_like(frame)
    grid = np.mean(grid, axis=-1)
    
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray_image)

    face_bb = None 
    if len(faces) == 0: 
        raise FaceNotFoundException()
    else: 
        face_bb = faces.pop(0)

    grid[face_bb.top():face_bb.bottom(), face_bb.left():face_bb.right()] = 255
    points = predictor(gray_image, face_bb)
    left_eye_points = points.parts()[42:48]
    right_eye_points = points.parts()[36:42]


    max_lep_x, max_lep_y, min_lep_x, min_lep_y = get_eye_bbox(left_eye_points)
    max_rep_x, max_rep_y, min_rep_x, min_rep_y = get_eye_bbox(right_eye_points)

    left_eye = frame[min_lep_y:max_lep_y, min_lep_x:max_lep_x]
    right_eye = frame[min_rep_y:max_rep_y, min_rep_x:max_rep_x]
    face = frame[face_bb.top():face_bb.bottom(), face_bb.left():face_bb.right()]
 
    rgb_grid = np.stack((grid,) * 3, axis=-1)   

    img = {
        "left": left_eye,
        "right":right_eye,
        "face": face,
        "grid": rgb_grid,
    }

    return img  
if __name__ == "__main__":
    if len(sys.argv) != 2: 
        print("This program expects one argument")
        sys.exit()

    image = cv2.imread(sys.argv[1])

    processed_image = process_frame(image)
    
    try: 
        os.mkdir('processed_image')
    except:
        print('outdir already exists')

    for key in processed_image.keys(): 
        # img = (processed_image[key] * 255).astype(np.uint8)
        if key != 'grid':
            img = cv2.cvtColor(processed_image[key], cv2.COLOR_BGR2RGB)
        else: 
            img = processed_image[key]
        print(img.shape)
        if not cv2.imwrite(f'./processed_image/{key}.png', img):
            print(f"Writing {key} to file failed")
        # if not cv2.imwrite(f'./processed_image/{key}.jpg', processed_image[key]):
        #     print(f"Writing {key} to file failed")



