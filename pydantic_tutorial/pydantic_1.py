# Import BaseModel to create Pydantic models
# EmailStr and AnyUrl are built-in validated data types
# Field is used to add constraints and metadata
from pydantic import BaseModel, EmailStr, AnyUrl, Field

# Import typing tools for type hints
# Annotated is used to attach Field metadata to types (Pydantic v2 style)
from typing import List, Dict, Optional, Annotated


# Define a Pydantic model (validated data structure)
class Patient(BaseModel):

    # Patient name
    # Must be a string with maximum length of 50 characters
    # title and description are mainly used by FastAPI documentation
    name: Annotated[
        str,
        Field(
            max_length=50,
            title="Name of the patient",
            description="Give the name of the patient in less than 50 characters"
        )
    ]

    # Email field
    # EmailStr automatically checks for valid email format
    email: EmailStr

    # Age field
    # Must be an integer greater than 0 and less than 120
    # Pydantic will convert string numbers to int automatically
    age: int = Field(gt=0, lt=120)

    # LinkedIn profile URL
    # AnyUrl ensures the value is a valid URL
    linkedin: AnyUrl

    # Weight field
    # Must be a float greater than 0
    # strict=True disables automatic string → float conversion
    weight: Annotated[
        float,
        Field(gt=0, strict=True)
    ]

    # Married status
    # Optional[bool] means it can be True, False, or None
    # Default value is None if not provided
    married: Annotated[
        Optional[bool],
        Field(
            default=None,
            description="Is the patient married or not"
        )
    ]

    # Allergies list
    # Optional list of strings
    # max_length limits number of items in the list
    allergies: Annotated[
        Optional[List[str]],
        Field(
            default=None,
            max_length=5
        )
    ]

    # Contact details
    # Dictionary where both keys and values must be strings
    contact_details: Dict[str, str]


# Function that accepts only a validated Patient object
def insert_patient_data(patient: Patient):

    # Print patient's name
    print(patient.name)

    # Print patient's age (already validated and converted)
    print(patient.age)

    # Print patient's allergies (can be None or list)
    print(patient.allergies)

    # Simulate inserting data into database
    print("inserted")


# Raw input data (untrusted, like JSON from an API request)
patient_info = {
    "name": "arjun",
    "email": "avb@gmail.com",
    "age": "20",                          # String → converted to int
    "linkedin": "http://linkedin.com/1233",
    "weight": 70.0,                       # Must be float due to strict=True
    "married": "False",                   # String → converted to bool
    "allergies": ["dust", "pollen"],
    "contact_details": {"phone": "2354678"}
}


# Create Patient object
# Pydantic validates, converts, and stores clean data
patient1 = Patient(**patient_info)


# Pass validated object to function
insert_patient_data(patient1)
