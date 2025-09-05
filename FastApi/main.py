# first create the virtual environment in the terminal of the folder with the command --> python -m venv venv
# activate the environment by running --> venv/scripts/activate
# install fastapi uvicorn (server) pydantic (data validation library) --> pip install fastapi uvicorn pydantic
# Start a local server for your FastAPI (or ASGI) app by running --> uvicorn main:app --reload
from fastapi import FastAPI, Path, HTTPException, Query
import json

from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal

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


#----------------------
#Post Request with Pydantic Concepts

class Patient(BaseModel):

    id: Annotated[str, Field(..., description='ID of the patient', examples=['P001'])]
    name: Annotated[str, Field(..., description='Name of the patient')]
    city: Annotated[str, Field(..., description='City where the patient is living')]
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the patient')]
    gender: Annotated[Literal['male', 'female', 'others'], Field(..., description='Gender of the patient')]
    height: Annotated[float, Field(..., gt=0, description='Height of the patient in mtrs')]
    weight: Annotated[float, Field(..., gt=0, description='Weight of the patient in kgs')]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:

        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Normal'
        else:
            return 'Obese'
        
def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f)        

@app.post('/create')
def create_patient(patient: Patient):

    # load existing data
    data = load_data()

    # check if the patient already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient already exists')

    # new patient add to the database
    data[patient.id] = patient.model_dump(exclude=['id'])

    # save into the json file
    save_data(data)

    return JSONResponse(status_code=201, content={'message':'patient created successfully'})
