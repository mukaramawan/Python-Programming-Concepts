# Install Pydantic by --> pip install pydantic

from pydantic import BaseModel

class patient(BaseModel):
    name: str
    age: int

def insert_patient(patient: patient):
    print(patient.name)
    print(patient.age)
    print("inserted!")

patient1 = {'name': 'Mukaram Awan', 'age': 18}

patient1 = patient(**patient1)

insert_patient(patient1)

