import numpy as np 
import dlib 
import cv2 
import torch 

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

    left_eye = cv2.resize(left_eye, (224, 224))
    left_eye = np.expand_dims(left_eye, axis=0)
    left_eye = np.transpose(left_eye, (0, 3, 1, 2))

    right_eye = cv2.resize(right_eye, (224, 224))
    right_eye = np.expand_dims(right_eye, axis=0)
    right_eye = np.transpose(right_eye, (0, 3, 1, 2))

    face = cv2.resize(face, (224, 224))
    face = np.expand_dims(face, axis=0)
    face = np.transpose(face, (0, 3, 1, 2))

    grid = cv2.resize(grid, (25, 25))
    grid = np.expand_dims(grid, 0)
    grid = np.expand_dims(grid, 0)

    img = {
        "left": torch.from_numpy(left_eye).type(torch.FloatTensor),
        "right": torch.from_numpy(right_eye).type(torch.FloatTensor),
        "face": torch.from_numpy(face).type(torch.FloatTensor),
        "grid": torch.from_numpy(grid).type(torch.FloatTensor),
    }

    return img  
