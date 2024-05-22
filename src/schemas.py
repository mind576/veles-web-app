import uuid
from typing import Optional,Union
from datetime import datetime,date
from fastapi_users import schemas
from pydantic import field_validator

from pydantic import (
    ValidationInfo,
    field_validator,
    BaseModel,
    Field,
    AliasChoices, 
    StrictBytes,
    StrictStr,
    ByteSize,
    EmailStr,
    FilePath
)


current_time = datetime.now()

# Base User
class UserRead(schemas.BaseUser[uuid.UUID]):
    phone_number: str


class UserCreate(schemas.BaseUserCreate):
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
    @field_validator('phone_number')
    @classmethod
    def check_numeric(cls, v: str, info: ValidationInfo) -> str:
        if isinstance(v, str):
            is_numeric = v.replace(' ', '').isnumeric()
            assert is_numeric, f'{info.field_name} phone number must be numeric'
        return v
    
 
    
    
    
    
class UserExtRead(BaseModel):
    user_id: uuid.UUID
    position: str
    company: str
    options: dict
    birth_date: bytes
    avatar: str
    full_name: str


class UserExtCreate(BaseModel):
    user_id: uuid.UUID
    position: str = Field()
    company: str =Field()
    options: Optional[dict] = Field()
    birth_date: Optional[datetime] = Field()
    avatar: Optional[Union[StrictStr,StrictBytes]] = Field()
    full_name: str = Field()
    

    
class UserExtUpdate(BaseModel):
    user_id: uuid.UUID
    position: str = Field(default=None)
    company: str =Field(default=None)
    options: Optional[dict] = Field(default=None)
    birth_date: Optional[datetime] = Field(default=None)
    avatar: Optional[Union[StrictStr,StrictBytes]] = Field(default=None)
    full_name: str = Field(default=None)
    
    
    
    
    
# Company Schemas
class CompanyCreate(BaseModel):
    company_name:   Optional[str] = Field()
    email: Optional[EmailStr] = Field()
    address: Optional[str] = Field()
    location: Optional[str] = Field()
    options: Optional[dict] = Field()
    credentials: Optional[dict] = Field()
    company_logo: Optional[Union[StrictStr,StrictBytes]] = Field()
    
class CompanyUpdate(BaseModel):
    company_name:   Optional[str] = Field()
    email: Optional[EmailStr] = Field()
    address: Optional[str] = Field()
    location: Optional[str] = Field()
    options: Optional[dict] = Field()
    credentials: Optional[dict] = Field()
    company_logo: Optional[Union[StrictStr,StrictBytes]] = Field()
    
    
class CompanyRead(BaseModel):
    id: uuid.UUID
    company_name:  str
    director: str
    email: EmailStr
    address: str
    location: str
    options: dict
    credentials: dict
    company_logo: Union[StrictStr,StrictBytes]
