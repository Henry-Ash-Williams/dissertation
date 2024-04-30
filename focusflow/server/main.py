from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from typing import Literal
from PIL import Image
from model import itracker_mobile, itracker_desktop
import cv2
import io 
import numpy as np
from process import process_frame, FaceNotFoundException
from rich import inspect
import torch

app = FastAPI() 

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],
    allow_credentials=False, 
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/sanity-check')
async def sanity_check():
    return {'sanity': 'verified'}

@app.post('/predict-gaze-location')
async def predict_gaze_location(file: UploadFile, mode: Literal["desktop", "mobile"] = "desktop"):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    image = np.array(image)

    try: 
        frame = process_frame(image)
        model = itracker_desktop if mode == "desktop" else itracker_mobile
        loc = model(frame).tolist()[0]
        print(loc)
        return {'location': {
            'x': loc[0],
            'y': loc[1] 
        }}
    except FaceNotFoundException: 
        return {'error': 'face not found in image'}
        


    