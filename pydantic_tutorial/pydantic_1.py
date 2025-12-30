from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated #we attach metadata by combo of annotated and fields


class Patient(BaseModel):

    name: Annotated[str,Field(max_length=50,title='Name of the patient',description='Give the name of the patient in less than 50 characters')]
    email: EmailStr #builtin custom datatype
    age: int =Field(gt=0,lt=120)#custom data validation , eg 0<age<60
    linkedin: AnyUrl
    weight: Annotated[float,Field(gt=0,strict=True)]
    married: Annotated[bool,Field(default=None,description='Is the patient marrei or not')]
    allergies : Annotated[Optional[List[str]],Field(default=None,max_length=5)] #making it optional and annotated
    contact_details: Dict[str,str]


def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print('inserted')

patient_info={'name':'arjun','email':'avb@gmail.com','age':'20','linkedin':'http://linkedin.com/1233','weight':'70','married':'False','allergies':['dust','gays'],'contact_details':{'phone':'2354678'}}

patient1=Patient(**patient_info)

insert_patient_data(patient1)