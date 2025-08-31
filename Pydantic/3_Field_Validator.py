from pydantic import BaseModel, EmailStr, field_validator
from typing import List, Dict, Optional

class patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    weight: float
    married: bool = False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

    # to ensure email should belongs to cui lahore or cui abbottabad

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['cuilhr.edu.pk', 'cuiatd.edu.pk']
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError("Not a valid email!")
        return value

    # Field validator for Transformation
    @field_validator('name')
    @classmethod
    def tansform_name(cls, name):
        return name.upper()
    
    #Two modes of field validator 1. before 2.after
    #In after mode field validator got value after type conversion

def insert_patient(patient: patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'Mukaram Awan', 'age': '18', 'email': 'mukaram@cuilhr.edu.pk', 'weight': 75.2,'married': True, 'allergies': ['pollen', 'dust'] ,'contact_details':{'phone':'123456789'}}

patient1 = patient(**patient_info)

insert_patient(patient1)
