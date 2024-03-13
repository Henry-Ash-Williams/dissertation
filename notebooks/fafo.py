import pandas as pd 
import numpy as np

loc = '/Volumes/x10-pro/MPIIFaceGaze_processed/Label'
file = 'p00.label'

df = pd.read_csv(f'{loc}/{file}', sep=' ')
labels = df['2DPoint']
ratio = df['ratio']

labels = np.array([np.array(point.split(',')).astype('float') for point in labels])
ratio = np.array([np.array(point.split(',')).astype('float') for point in labels])

model_inputs = labels * ratio * 0.01
print(model_inputs)