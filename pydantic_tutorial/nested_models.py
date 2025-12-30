from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str


class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address

address_dict={'city':'Mandsaur','state':'Madhya pradesh','pin':'458001'}

address1 = Address(**address_dict) #address pydantic model ka object bana lia, dict  ko open krke

patient_dict = {'name':'nitish','gender':'male','age':35 , 'address':address1}

patient1= Patient(**patient_dict)

print(patient1)
print(patient1.name)
print(patient1.address.city)



#benefits
#1. Better organization of related data 
#2. Reusability : use vitals in multiple models
#3. Redability: easeir for developers and API consumers to understand
#4. Validation : Nested models are validated automatically - no extra work needed