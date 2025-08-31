from pydantic import BaseModel

class Address(BaseModel):
    House: str
    Street: str
    city: str
    pincode: str

class Patient(BaseModel):
    name: str
    age: int = None
    address: Address


address_dict = {
    'House': '10',
    'Street': '10',
    'city': 'Gujranwala',
    'pincode': '22250'
}

address1 = Address(**address_dict)

patient_dict = {
    'name': 'Mukaram',
    # 'age': 23,
    'address': address1
}

patient1 = Patient(**patient_dict)

print(patient1.name)
print(patient1.address)
print(patient1.address.city)


# Better organization of related data (e.g., vitals, address, insurance)
# Reusability: Use Vitals in multiple models (e.g., Patient, MedicalRecord)
# Readability: Easier for developers and API consumers to understand
# Validation: Nested models are validated automatically—no extra work needed


# Serialization

temp = patient1.model_dump()
print(temp)
print(type(temp))

temp = patient1.model_dump_json()
print(temp)
print(type(temp))

temp = patient1.model_dump(include=['name'])
print(temp)

temp = patient1.model_dump(exclude=['name'])
print(temp)

temp = patient1.model_dump(exclude={'address':['pincode']})
print(temp)

temp = patient1.model_dump(exclude_unset=False)
print(temp)