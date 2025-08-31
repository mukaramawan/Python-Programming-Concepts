#A computed field is a field that doesn’t exist in the input data but is computed dynamically from other fields

from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict, Optional

class patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    height: float
    weight: float
    married: bool = False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi


def insert_patient(patient: patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print("BMI: ",patient.bmi)
    print('updated')

patient_info = {'name':'Mukaram Awan', 'age': '65', 'email': 'mukaram@cuilhr.edu.pk', 'height': '1.72', 'weight': 75.2,'married': True, 'allergies': ['pollen', 'dust'] ,'contact_details':{'phone':'123456789', 'emergency': '123456789'}}

patient1 = patient(**patient_info)

insert_patient(patient1)
