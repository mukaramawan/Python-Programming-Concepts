#Use when your validation logic depends on multiple fields.

from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict, Optional

class patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    weight: float
    married: bool = False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]


    @model_validator(mode='after')
    def valid_emergency_contact(cls, model):
        if model.age >= 60 and 'emergency' not in model.contact_details:
            raise ValueError("Patients older than 60 must have emergency contact!")
        return model

def insert_patient(patient: patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'Mukaram Awan', 'age': '65', 'email': 'mukaram@cuilhr.edu.pk', 'weight': 75.2,'married': True, 'allergies': ['pollen', 'dust'] ,'contact_details':{'phone':'123456789', 'emergency': '123456789'}}

patient1 = patient(**patient_info)

insert_patient(patient1)
