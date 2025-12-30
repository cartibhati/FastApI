from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator
from typing import List,Dict,Optional,Annotated 


class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies : List[str]
    contact_details: Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')

        return value

def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print('inserted')

patient_info={'name':'arjun','email':'avb@hdfc.com','age':'20','weight':'70','married':'False','allergies':['dust','gays'],'contact_details':{'phone':'2354678'}}

patient1=Patient(**patient_info)#validation->type-coercion 

insert_patient_data(patient1)