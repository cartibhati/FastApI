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
#______________________________________________________________________________________________________________

temp=patient1.model_dump()
print(temp)
print(type(temp))

temp2=patient1.model_dump(include=['name','gender'])
print(temp2)

temp1=patient1.model_dump_json
print(type(temp1))