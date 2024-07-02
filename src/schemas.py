import uuid
from typing import Optional,Union,AnyStr,Any,List
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
    birth_date: date


class UserCreate(schemas.BaseUserCreate):
    full_name: str = Field()
    email: str = Field()
    phone: str = Field()
    picture: str = Field(default=None)
    birth_date: date | None
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
    picture: str = Field()
    birth_date: date | None
    @field_validator('phone')
    @classmethod
    def check_numeric(cls, v: str, info: ValidationInfo) -> str:
        if isinstance(v, str):
            is_numeric = v.replace(' ', '').isnumeric()
            assert is_numeric, f'{info.field_name} phone number must be numeric'
        return v
    
 


# E M P L O Y E E     S C H E M A S

class EmployeeRead(BaseModel):
    user_id: int
    position: str
    obligations: bytes
    company_id: int
    company: str




class EmployeeCreate(BaseModel):
    user_id: Optional[int] = Field(default=None)
    position: Optional[str] = Field(default=None)
    obligations: Optional[str] = Field(default=None)
    company_id: Optional[int] = Field()


    
    
class EmployeeUpdate(BaseModel):
    position: Optional[str] = Field(default=None)
    obligations: Optional[str] = Field(default=None)
    company_id: Optional[int] = Field()
    # option_one: Optional[List] = Field(default=None)
    # option_two: Optional[List] = Field(default=None)
    
    
# Company Schemas
class CompanyCreate(BaseModel):
    name: Optional[str] = Field()
    phone: Optional[str] = Field()
    email: Optional[EmailStr] = Field()
    address: Optional[str] = Field()
    location: Optional[str] = Field()
    info: Optional[str] = Field()
    type: Optional[str] = Field()
    name_legal: Optional[str] = Field()
    INN: Optional[str] = Field()
    KPP: Optional[str] = Field()
    OGRN: Optional[str] = Field()
    OKPO: Optional[str] = Field()
    BIK: Optional[str] = Field()
    bank_name: Optional[str] = Field()
    bank_address: Optional[str] = Field()
    corr_account: Optional[str] = Field()
    employees: List = None
    @field_validator('phone')
    @classmethod
    def check_numeric(cls, v: str, info: ValidationInfo) -> str:
        if isinstance(v, str):
            is_numeric = v.replace(' ', '').isnumeric()
            assert is_numeric, f'{info.field_name} phone number must be numeric'
        return v

    
class CompanyUpdate(BaseModel):
    name: Optional[str] = Field()
    phone: Optional[str] = Field()
    email: Optional[EmailStr] = Field()
    address: Optional[str] = Field()
    location: Optional[str] = Field()
    info: Optional[str] = Field()
    type: Optional[str] = Field()
    name_legal: Optional[str] = Field()
    INN: Optional[str] = Field()
    KPP: Optional[str] = Field()
    OGRN: Optional[str] = Field()
    OKPO: Optional[str] = Field()
    BIK: Optional[str] = Field()
    bank_name: Optional[str] = Field()
    bank_address: Optional[str] = Field()
    corr_account: Optional[str] = Field()
    employees: List
    @field_validator('phone')
    @classmethod
    def check_numeric(cls, v: str, info: ValidationInfo) -> str:
        if isinstance(v, str):
            is_numeric = v.replace(' ', '').isnumeric()
            assert is_numeric, f'{info.field_name} phone number must be numeric'
        return v

    
    
class CompanyRead(BaseModel):
    id: int
    name: str 
    director: int 
    phone: str 
    email: EmailStr
    address: str 
    location: str 
    info: str 
    type: str 
    name_legal: str 
    INN: str 
    KPP: str 
    OGRN: str 
    OKPO: Optional[ str | None ]
    BIK: str 
    bank_name: str 
    bank_address: str 
    corr_account: str 
    employees: Optional[ List | None ]

