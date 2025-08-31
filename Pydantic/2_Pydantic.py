# Install Pydantic by --> pip install pydantic

from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class patient(BaseModel):
    #name: str = Field(max_length=20)
    name: Annotated[str, Field(max_length=20, title='Name of Patient', description='Enter the name of the patient less than 20 chars!', examples=['Mukaram Awan', 'Muhammad Mukaram'])]
    age: int
    email: EmailStr
    linkedin: AnyUrl
    # weight: float = Field(gt=0)
    weight: Annotated[float, Field(gt=0, strict=True)]  #now can't handle '75.2'
    married: bool = False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

def insert_patient(patient: patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'Mukaram Awan', 'age': '18', 'email': 'mukaram@gmail.com','linkedin': 'https://www.linkedin.com/in/mukaram-awan/', 'weight': 75.2,'married': True, 'contact_details':{'phone':'123456789'}}

patient1 = patient(**patient_info)

insert_patient(patient1)

