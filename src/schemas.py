import uuid
from typing import Optional
from datetime import datetime
from fastapi_users import schemas
from pydantic import field_validator
from pydantic import (
    ValidationInfo,
    field_validator,
    BaseModel,
    Field
)

current_time = datetime.now()


class UserExtRead(BaseModel):
    user_id: int
    position: str
    company: str
    options: dict


# id: Mapped[int] = mapped_column(primary_key=True)
#     user_id: Mapped[int] = mapped_column(ForeignKey("users_table.id"))
#     position: Mapped[Optional[str]] = mapped_column(String)
#     company: Mapped[Optional[str]] = mapped_column(String)
#     options: Mapped[Optional[dict]] = mapped_column(JSON)
class UserExtCreate(BaseModel):
    user_id: int
    position: str
    company: str
    options: Optional[dict]
    
class UserExtUpdate(BaseModel):
    user_id: int
    position: str
    company: str
    options: Optional[dict]

    
    

class UserRead(schemas.BaseUser[uuid.UUID]):
    phone_number: str


class UserCreate(schemas.BaseUserCreate):
    phone_number: str 
    registred_date: Optional[str] = current_time
    @field_validator('phone_number')
    @classmethod
    def check_numeric(cls, v: str, info: ValidationInfo) -> str:
        if isinstance(v, str):
            is_numeric = v.replace(' ', '').isnumeric()
            assert is_numeric, f'{info.field_name} phone number must be numeric'
        return v





class UserUpdate(schemas.BaseUserUpdate):
    company: str
    phone_number: str
    @field_validator('phone_number')
    @classmethod
    def check_numeric(cls, v: str, info: ValidationInfo) -> str:
        if isinstance(v, str):
            is_numeric = v.replace(' ', '').isnumeric()
            assert is_numeric, f'{info.field_name} phone number must be numeric'
        return v