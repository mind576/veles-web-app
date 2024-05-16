import uuid

from fastapi_users import schemas
from pydantic import field_validator
from pydantic import (
    ValidationInfo,
    field_validator,
)




class UserRead(schemas.BaseUser[uuid.UUID]):
    position: str 
    company: str
    phone_number: str


class UserCreate(schemas.BaseUserCreate):
    position: str 
    company: str
    phone_number: str 
    @field_validator('phone_number')
    @classmethod
    def check_numeric(cls, v: str, info: ValidationInfo) -> str:
        if isinstance(v, str):
            is_numeric = v.replace(' ', '').isnumeric()
            assert is_numeric, f'{info.field_name} phone number must be numeric'
        return v


class UserUpdate(schemas.BaseUserUpdate):
    position: str 
    company: str
    phone_number: str
    @field_validator('phone_number')
    @classmethod
    def check_numeric(cls, v: str, info: ValidationInfo) -> str:
        if isinstance(v, str):
            is_numeric = v.replace(' ', '').isnumeric()
            assert is_numeric, f'{info.field_name} phone number must be numeric'
        return v