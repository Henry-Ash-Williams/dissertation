from fastapi import FastAPI 
from model import ITrackerModel
import torch 

MODEL_PATH = "TODO"

app = FastAPI() 

model = None

@app.get('/model-status')
def status():
    return {'status': 'online' if model is not None else 'offline'} 

@app.get('/load-model')
def load():
    global model 

    if status()['status'] == 'online':
        return {'error': 'model already loaded'}
    else: 
        model = ITrackerModel()
        model = torch.load_state_dict(torch.load(MODEL_PATH))
        return status()
    
    