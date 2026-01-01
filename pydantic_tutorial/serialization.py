from pydantic import BaseModel


# Address is a nested Pydantic model
class Address(BaseModel):
    city: str
    state: str
    pin: str


# Patient model contains Address as a field
class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address


# Normal dictionary for address data
address_dict = {
    'city': 'Mandsaur',
    'state': 'Madhya pradesh',
    'pin': '458001'
}

# Creating Address model object
# Dict ko ** open karke Address model me pass kiya
address1 = Address(**address_dict)


# Patient dictionary
# address field me hum Address model ka object de rahe hain
patient_dict = {
    'name': 'nitish',
    'gender': 'male',
    'age': 35,
    'address': address1
}

# Creating Patient model object
patient1 = Patient(**patient_dict)

# -------------------------------------------------------------
# model_dump()
# -------------------------------------------------------------

# model_dump() converts the Pydantic model into a normal Python dict
# ✔ Nested models are also converted into dicts
# ✔ Useful for DB insert, API response, logging, etc.
temp = patient1.model_dump()

print(temp)        # Output will be a dictionary
print(type(temp))  # <class 'dict'>


# model_dump(include=[...])
# Only selected fields will be included in the output
# ✔ address and age will be ignored here
temp2 = patient1.model_dump(include=['name', 'gender'])
print(temp2)


# -------------------------------------------------------------
# model_dump_json
# -------------------------------------------------------------

# model_dump_json is a METHOD (function reference)
# ❌ You forgot to call it with ()
temp1 = patient1.model_dump_json

print(type(temp1))  # <class 'method'>
