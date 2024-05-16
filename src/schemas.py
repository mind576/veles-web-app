import uuid

from fastapi_users import schemas
from pydantic import BaseModel,field_validator
from pydantic.types import constr




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
    def phone_number_must_contain_plus(cls, v: str) -> str:
        prefix = '+7'
        if not cls.phone_number.starts_with(prefix):
            raise ValueError('Must contain a +7')
        return v.title()


#str.startswith(prefix[, start[, end]])

class UserUpdate(schemas.BaseUserUpdate):
    position: str 
    company: str
    phone_number: str
    @field_validator('phone_number')
    @classmethod
    def phone_number_must_contain_plus(cls, v: str) -> str:
        prefix = '+7'
        if not cls.phone_number.starts_with(prefix):
            raise ValueError('Must contain a +7')
        return v.title()
