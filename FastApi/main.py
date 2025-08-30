# first create the virtual environment in the terminal of the folder with the command --> python -m venv venv
# activate the environment by running --> venv/scripts/activate
# install fastapi uvicorn (server) pydantic (data validation library) --> pip install fastapi uvicorn pydantic
# Start a local server for your FastAPI (or ASGI) app by running --> uvicorn main:app --reload
from fastapi import FastAPI, Path, HTTPException, Query
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

#----------------------
#Path & Query Parameter, Http Exceptions

#path parameter
@app.get('/patients/{patient_id}')
def viewPatient(patient_id: str = Path(..., description="Id of the Patient", example='P001')):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found!")

#query parameter
@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description="Sort on the basis of height, weight, bmi"), order: str = Query('asc', description="Sort in asc or desc order")):

    valid_fields = ['height', 'weight', 'bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid Field: Select from {valid_fields}')
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400, detail='Invalid order: select asc, desc order!')
    
    data = load_data()
    sort_order = True if order=='desc' else False
    sorted_data = sorted(data.values(), key = lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data

