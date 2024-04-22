import numpy as np 
import torch 
from model import ITrackerModel
import cv2 
import dlib 
import matplotlib.pyplot as plt 
import time 

class FaceNotFoundException(Exception):
    def __init__(self, message="Could not find a face in this image"):
        self.message = message 
        super().__init__(self.message)

MODEL_PATH = "/Users/henrywilliams/Documents/uni/dissertation/focusflow/server/Iter_25_Itracker_mpii.pt"

SHOW_INPUT_IMAGES = False 

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("/Users/henrywilliams/Documents/uni/dissertation/other-work/shape_predictor_68_face_landmarks.dat")

def process_frame(frame: np.ndarray) -> dict:
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


    max_lep_x = max(left_eye_points, key=lambda point: point.x).x
    max_lep_y = max(left_eye_points, key=lambda point: point.y).y
    min_lep_x = min(left_eye_points, key=lambda point: point.x).x
    min_lep_y = min(left_eye_points, key=lambda point: point.y).y

    max_rep_x = max(right_eye_points, key=lambda point: point.x).x
    max_rep_y = max(right_eye_points, key=lambda point: point.y).y
    min_rep_x = min(right_eye_points, key=lambda point: point.x).x
    min_rep_y = min(right_eye_points, key=lambda point: point.y).y

    left_eye = frame[min_lep_y:max_lep_y, min_lep_x:max_lep_x]
    right_eye = frame[min_rep_y:max_rep_y, min_rep_x:max_rep_x]
    face = frame[face_bb.top():face_bb.bottom(), face_bb.left():face_bb.right()]

    if SHOW_INPUT_IMAGES:
        plt.subplot(2,2,1) 
        plt.imshow(left_eye)
        plt.title("Left Eye")
        plt.axis("off")
        plt.subplot(2,2,2) 
        plt.imshow(right_eye)
        plt.title("Right Eye")
        plt.axis("off")
        plt.subplot(2,2,3) 
        plt.imshow(face)
        plt.title("Face")
        plt.axis("off")
        plt.subplot(2,2,4) 
        plt.imshow(grid)
        plt.title("Binary Mask")
        plt.axis("off")
        plt.show()

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

if __name__ == "__main__":
    model = ITrackerModel()

    model.load_state_dict(torch.load(MODEL_PATH))
    model.eval()
    cap = cv2.VideoCapture(0)

    predicitons = []


    if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()

    while True:
        try: 
            ret, frame = cap.read()
            try: 
                start = time.time()
                frame = process_frame(frame)
                end = time.time()
            except FaceNotFoundException: 
                # Face not found 
                print("face not found in image")
                continue

            # Check if the frame was successfully captured
            if not ret:
                print("Error: Could not read frame.")
                break

            predicitons.append(model(frame))
            
            # # Exit the loop when the 'q' key is pressed
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break
        except KeyboardInterrupt: 
            break 

    cap.release()
    cv2.destroyAllWindows()
    predictions = np.array([tensor.detach().numpy()[0] for tensor in predicitons])
    grid_size = 100
    heatmap, xedges, yedges = np.histogram2d(predictions[:, 0], predictions[:, 1], bins=grid_size)    
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    plt.imshow(heatmap.T, extent=extent, origin='lower', cmap='hot')
    plt.colorbar(label='Frequency of iTracker predictions')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Heatmap of Gaze Locations')
    plt.show()