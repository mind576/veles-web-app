import uuid
from typing import Optional,Union,AnyStr,Any
from datetime import datetime
from fastapi_users import schemas
from pydantic import field_validator,Field

from pydantic import (
    ValidationInfo,
    field_validator,
    BaseModel,
    Field,
    EmailStr,
)


current_time = datetime.now()




# Base User
class UserRead(schemas.BaseUser[int]):
    full_name: str
    phone_number: str


class UserCreate(schemas.BaseUserCreate):
    full_name: str
    phone_number: str 
    @field_validator('phone_number')
    @classmethod
    def check_numeric(cls, v: str, info: ValidationInfo) -> str:
        if isinstance(v, str):
            is_numeric = v.replace(' ', '').isnumeric()
            assert is_numeric, f'{info.field_name} phone number must be numeric'
        return v





class UserUpdate(schemas.BaseUserUpdate):
    phone_number: str
    full_name: str
    @field_validator('phone_number')
    @classmethod
    def check_numeric(cls, v: str, info: ValidationInfo) -> str:
        if isinstance(v, str):
            is_numeric = v.replace(' ', '').isnumeric()
            assert is_numeric, f'{info.field_name} phone number must be numeric'
        return v
    
 
    
    
    
    
class UserExtRead(BaseModel):
    user_id: int
    profession: str
    birth_date: bytes

    


class UserExtCreate(BaseModel):
    profession: str = Field()
    birth_date: Optional[str] = Field()
    
    

    
class UserExtUpdate(BaseModel):
    profession: str = Field(default=None)
    birth_date: Optional[str] = Field()

    
    
    
    
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

