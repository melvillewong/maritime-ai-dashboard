## Requirements

- python3
- pip
- venv

## Setup

1. `python3 -m venv backend/.env` to isolate project dependencies in virtual environment
2. `source backend/.env/bin/activate` (Linux/MacOS) or `.venv\Scripts\activate` (Windows), to activate VM
3. `python3 -m pip install -r backend/requirements.txt` to install required dependencies

## Run fastAPI

1. `uvicorn backend.app.main:app --reload`
2. Search http://localhost:8000/docs with your browser
