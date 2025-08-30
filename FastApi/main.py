# first create the virtual environment in the terminal of the folder with the command --> python -m venv venv
# activate the environment by running --> venv/scripts/activate
# install fastapi uvicorn (server) pydantic (data validation library) --> pip install fastapi uvicorn pydantic
# Start a local server for your FastAPI (or ASGI) app by running --> uvicorn main:app --reload
from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)

    return data

@app.get("/")
def Hello():
    return {"message": "Patients Management System!"}

@app.get("/about")
def about():
    return {"message": "Hello! This is Eye Care Center!"}

@app.get('/patients')
def view():
    data = load_data()

    return data
