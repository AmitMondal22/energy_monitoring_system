from pydantic import BaseModel, Field, constr, validator
from datetime import date

class Register(BaseModel):
    name: str
    email: str
    user_type: str
    password: str
    confirm_password: str

    @validator('user_type')
    def validate_user_type(cls, v):
        valid_user_types = {"A", "S", "U", "C"}
        # valid_user_types = {"A", "SA", "U", "C"}
        if v not in valid_user_types:
            raise ValueError('Invalid user type')
        return v

    @validator('confirm_password')
    def passwords_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError('Passwords do not match')
        return v





class Login(BaseModel):
    email: str
    password: str