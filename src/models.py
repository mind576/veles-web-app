from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from fastapi_users.db import SQLAlchemyBaseUserTable
from settings import *
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy import String, Date, ForeignKey,LargeBinary,Integer,Boolean
from datetime import date
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
import uuid


Base: DeclarativeMeta = declarative_base()

UUID_ID = uuid.UUID


class User(SQLAlchemyBaseUserTable[int], Base):
    """
    User table with obvious and visible fields and options.
    """
    __tablename__ = 'users_table'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    full_name: Mapped[str] = mapped_column(String,nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    phone_number: Mapped[str] = mapped_column(String, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=True, default=True)
    is_superuser: Mapped[bool] = mapped_column(Boolean, nullable=True, default=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, nullable=True, default=False)

    def __repr__(self):
        return f"User= {self.full_name} {self.id} "



class UserExtension(Base):
    """ User Extension ORM model:\n
    This model extends class User and helps to store additional data fields .

    """
    __tablename__ = 'user_extension'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users_table.id"))
    profession: Mapped[Optional[str]] = mapped_column(String,nullable=True)
    options_dict: Mapped[Optional[dict]] = mapped_column(JSONB,nullable=True)
    birth_date: Mapped[date.fromisoformat] = mapped_column(Date,nullable=True)
    avatar: Mapped[Optional[bytes]] = mapped_column(LargeBinary,nullable=True)
    def __repr__(self):
        return f"UserExtension_users_id={self.user_id}   company_name={self.company} "
    
    
    
class Company(Base):
    """ Company ORM model:
    -- This model helps to store Company item data fields .
    Args:
        Base (SQLAlchemy Base class): 
    Returns:
        Company ORM Model:
    """
    __tablename__ = 'company_table'
    id: Mapped[int] = mapped_column(primary_key=True)
    company_name: Mapped[Optional[str]] = mapped_column(String)
    director: Mapped[Optional[int]] = mapped_column(ForeignKey("users_table.id")) # How many directors may run business ??
    email: Mapped[Optional[str]] = mapped_column(String)
    address: Mapped[Optional[str]] = mapped_column(String)
    location: Mapped[Optional[str]] = mapped_column(String)
    options_dict: Mapped[Optional[dict]] = mapped_column(JSONB,nullable=True)
    credentials: Mapped[Optional[dict]] = mapped_column(JSONB,nullable=True)
    company_logo: Mapped[Optional[bytes]] = mapped_column(LargeBinary,nullable=True)
    def __repr__(self):
        return f"Company Name={self.user_id} company_id={self.id}"