#!/bin/bash 

curl -X POST -F 'method=desktop' -F 'file=@/Users/henrywilliams/Documents/uni/dissertation/focusflow/server/example.jpg' "localhost:8000/predict-gaze-location"