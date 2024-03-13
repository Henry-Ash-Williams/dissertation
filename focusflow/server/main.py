from fastapi import FastAPI, File, UploadFile
from typing import Literal
from PIL import Image
from model import itracker_mobile, itracker_desktop
import cv2
import io 
import numpy as np
from process import process_frame
from rich import inspect

app = FastAPI() 

@app.get('/sanity-check')
async def sanity_check():
    return {'sanity': 'verified'}

@app.post('/predict-gaze-location')
async def predict_gaze_location(file: UploadFile, mode: Literal["desktop", "mobile"] = "desktop"):
    contents = await file.read()
    print(contents)
    image = Image.open(io.BytesIO(contents))
    image = np.array(image)
    frame = process_frame(image)

    match mode: 
        case "desktop":
            return {'location': itracker_desktop(frame)}
        case "mobile":
            return {'location': itracker_mobile(frame)}