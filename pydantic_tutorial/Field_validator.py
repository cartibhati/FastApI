# Import BaseModel to create data models with validation
# EmailStr is a special type that validates email format
# AnyUrl, Field are imported but not used here (good to know they exist)
# field_validator is used to create custom validation logic
from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator

# Import typing helpers for type hints
# List -> for list of items
# Dict -> for key-value pairs
# Optional -> for optional fields (can be None)
# Annotated -> advanced typing (not used here)
from typing import List, Dict, Optional, Annotated 


# Patient class inherits from BaseModel
# BaseModel automatically:
# 1. Validates data
# 2. Converts data types (type coercion)
# 3. Raises errors if data is invalid
class Patient(BaseModel):

    # name must be a string
    name: str

    # email must be a valid email format
    # Example: abc@gmail.com
    email: EmailStr

    # age must be an integer
    age: int

    # weight must be a float
    weight: float

    # married must be boolean (True/False)
    married: bool

    # allergies must be a list of strings
    allergies: List[str]

    # contact_details must be a dictionary with string keys and values
    contact_details: Dict[str, str]


    # ---------------- FIELD VALIDATOR ----------------
    # field_validator('email') means:
    # 👉 This function will run ONLY for the 'email' field
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        # Allowed email domains
        valid_domains = ['hdfc.com', 'icici.com']

        # Extract domain name from email
        # Example: avb@hdfc.com → hdfc.com
        domain_name = value.split('@')[-1]

        # Check if domain is allowed
        if domain_name not in valid_domains:
            # If not allowed, raise an error
            raise ValueError('Not a valid domain')

        # If validation passes, return the email
        return value


# Function that accepts only a Patient object
def insert_patient_data(patient: Patient):
    # Print patient's name
    print(patient.name)

    # Print patient's age
    print(patient.age)

    # Print patient's allergies
    print(patient.allergies)

    # Confirmation message
    print('inserted')


# Raw input data (mostly strings)
patient_info = {
    'name': 'arjun',
    'email': 'avb@hdfc.com',
    'age': '20',          # string → will be converted to int
    'weight': '70',       # string → will be converted to float
    'married': 'False',   # string → will be converted to bool
    'allergies': ['dust', 'gays'],
    'contact_details': {'phone': '2354678'}
}


# Creating Patient object
# Here Pydantic does:
# 1. Validation
# 2. Type coercion (string → int/float/bool)
# 3. Runs field validators
patient1 = Patient(**patient_info)


# Passing validated Patient object to function
insert_patient_data(patient1)
