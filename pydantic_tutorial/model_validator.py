from pydantic import BaseModel,EmailStr,AnyUrl,Field,model_validator
from typing import List,Dict,Optional,Annotated 


class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies : List[str]
    contact_details: Dict[str,str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age>60 and 'emergency' not in model.contact_details:
            raise ValueError('patients older than 60 must have an emergency contact')
        return model

def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print('inserted')

patient_info={'name':'arjun','email':'avb@hdfc.com','age':'20','weight':'70','married':'False','allergies':['dust','gays'],'contact_details':{'phone':'2354678','emergency':'8838828282'}}

patient1=Patient(**patient_info)#validation->type-coercion 

insert_patient_data(patient1)