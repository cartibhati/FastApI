from pydantic import BaseModel,EmailStr,AnyUrl,Field,model_validator,computed_field
from typing import List,Dict,Optional,Annotated 


class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    height: float
    married: bool
    allergies : List[str]
    contact_details: Dict[str,str]

    @computed_field
    @property
    def  bmi(self)->float:
        bmi = round(self.weight/(self.height**2))
        return bmi


def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print('inserted')
    print('BMI',patient.bmi)

patient_info={'name':'arjun','email':'avb@hdfc.com','age':'20','weight':'70','height':1.72,'married':'False','allergies':['dust','gays'],'contact_details':{'phone':'2354678','emergency':'8838828282'}}

patient1=Patient(**patient_info)#validation->type-coercion 

insert_patient_data(patient1)