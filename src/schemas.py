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


current_time = datetime.now()


# id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     full_name: Mapped[str] = mapped_column(String,nullable=False)
#     email: Mapped[str] = mapped_column(String, unique=True,nullable=False)
#     phone: Mapped[str] = mapped_column(String,unique=True, nullable=False)
#     picture: Mapped[str] = mapped_column(String)
#     birth_date: Mapped[date] = mapped_column(DateTime,nullable=True)
#     hashed_password: Mapped[str] = mapped_column(String, nullable=False)
#     is_active: Mapped[bool] = mapped_column(Boolean, default=True)
#     is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)
#     is_verified: Mapped[bool] = mapped_column(Boolean, default=False)


# Base User
class UserRead(schemas.BaseUser[int]):
    full_name: str
    email: str
    phone: str
    picture: str
    birth_date: str


class UserCreate(schemas.BaseUserCreate):
    full_name: str = Field()
    email: str = Field()
    phone: str = Field()
    picture: str = Field(default=None)
    birth_date: date = Field(default=None)
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
    phone: str
    picture: str
    birth_date: date = Field()
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
    position: str = Field()
    obligations: Optional[str] = Field()
    
    

    
class EmployeeUpdate(BaseModel):
    position: str = Field()
    obligations: Optional[str] = Field()
    

    
    
    
    
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

