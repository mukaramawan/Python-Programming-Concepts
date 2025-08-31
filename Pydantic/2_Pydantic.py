# Install Pydantic by --> pip install pydantic

from pydantic import BaseModel
from typing import List, Dict, Optional

class patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool = False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

def insert_patient(patient: patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'Mukaram Awan', 'age': '18', 'weight': 75.2,'married': True, 'contact_details':{'phone':'123456789'}}

patient1 = patient(**patient_info)

insert_patient(patient1)

