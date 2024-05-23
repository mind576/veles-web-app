import uuid
from typing import Optional,Union,AnyStr,Any
from datetime import datetime
from fastapi_users import schemas
from pydantic import field_validator, Json,Field

from pydantic import (
    ValidationInfo,
    field_validator,
    BaseModel,
    Field,
    StrictBytes,
    StrictStr,
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
    options_dict: dict
    birth_date: bytes
    avatar: str
    


class UserExtCreate(BaseModel):
    profession: str = Field()
    options_dict: Optional[Json] = Field()
    birth_date: Optional[str] = Field()
    avatar: Optional[Union[AnyStr]] = Field(default=Any)
    
    

    
class UserExtUpdate(BaseModel):
    profession: str = Field(default=None)
    options_dict: Optional[Json] = Field()
    birth_date: Optional[str] = Field()
    avatar: Optional[Union[AnyStr]] = Field(default=Any)
    
    
    
class Test(BaseModel):
    js: Json= Field()
    
# Company Schemas
class CompanyCreate(BaseModel):
    company_name: Optional[str] = Field()
    email: Optional[EmailStr] = Field()
    address: Optional[str] = Field()
    location: Optional[str] = Field()
    options_dict: Optional[dict] = Field()
    credentials: Optional[dict] = Field()
    company_logo: Optional[Union[StrictStr,StrictBytes]] = Field()
    
class CompanyUpdate(BaseModel):
    company_name:   Optional[str] = Field()
    email: Optional[EmailStr] = Field()
    address: Optional[str] = Field()
    location: Optional[str] = Field()
    options_dict: Optional[dict] = Field()
    credentials: Optional[dict] = Field()
    company_logo: Optional[Union[StrictStr,StrictBytes]] = Field()
    
    
class CompanyRead(BaseModel):
    id: int
    company_name:  str
    director: str
    email: EmailStr
    address: str
    location: str
    options_dict: dict
    credentials: dict
    company_logo: Union[StrictStr,StrictBytes]
