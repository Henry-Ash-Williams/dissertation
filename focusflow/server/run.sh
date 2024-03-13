#!/bin/sh 

activate() {
    if [ "$(which pip)" = "$HOME/.local/bin/pip" ]; then 
        echo "Activating virtual environment"
        . "$HOME/Documents/uni/dissertation/focusflow/server/.server-venv/bin/activate"
        return 0
    else
        echo "Virtual environment already active" 
        return 0 
    fi 
}

activate 
uvicorn --reload main:app 