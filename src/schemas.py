import uuid
from typing import Optional,Union,AnyStr,Any
from datetime import datetime, date
from fastapi_users import schemas
from pydantic import field_validator,Field

from pydantic import (
    ValidationInfo,
    field_validator,
    BaseModel,
    Field,
    EmailStr,
)



# Base User
class UserRead(schemas.BaseUser[int]):
    full_name: str
    email: str
    phone: str
    picture: str
    birth_date: datetime


class UserCreate(schemas.BaseUserCreate):
    full_name: str = Field()
    email: str = Field()
    phone: str = Field()
    picture: str = Field(default=None)
    birth_date: datetime | None
    @field_validator('phone')
    @classmethod
    def check_numeric(cls, v: str, info: ValidationInfo) -> str:
        if isinstance(v, str):
            is_numeric = v.replace(' ', '').isnumeric()
            assert is_numeric, f'{info.field_name} phone number must be numeric'
        return v





class UserUpdate(schemas.BaseUserUpdate):
    full_name: str = Field()
    email: str = Field()
    phone: str = Field()
    picture: str= Field()
    birth_date: datetime | None
    @field_validator('phone')
    @classmethod
    def check_numeric(cls, v: str, info: ValidationInfo) -> str:
        if isinstance(v, str):
            is_numeric = v.replace(' ', '').isnumeric()
            assert is_numeric, f'{info.field_name} phone number must be numeric'
        return v
    
 
class EmployeeRead(BaseModel):
    user_id: int
    position: str
    obligations: bytes

class EmployeeCreate(BaseModel):
    position: Optional[ str ] = Field(default=None)
    obligations: Optional[ str ] = Field(default=None)
    
    
class EmployeeUpdate(BaseModel):
    position: Optional[str] = Field(default=None)
    obligations: Optional[str] = Field(default=None)
    
    
# Company Schemas
class CompanyCreate(BaseModel):
    company_name: Optional[str] = Field()
    email: Optional[EmailStr] = Field()
    address: Optional[str] = Field()
    location: Optional[str] = Field()

    
class CompanyUpdate(BaseModel):
    company_name:   Optional[str] = Field()
    email: Optional[EmailStr] = Field()
    address: Optional[str] = Field()
    location: Optional[str] = Field()

    
    
class CompanyRead(BaseModel):
    id: int
    company_name:  str
    director: str
    email: EmailStr
    address: str
    location: str

