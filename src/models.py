from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from settings import *
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy import String, Date, ForeignKey,JSON, LargeBinary
from datetime import date
from sqlalchemy.dialects.postgresql import ARRAY
import uuid


Base: DeclarativeMeta = declarative_base()

UUID_ID = uuid.UUID


class User(SQLAlchemyBaseUserTableUUID, Base):
    """
    User table - basic User ORM model that helps perform Authentification and OAuth needs.
    """
    __tablename__ = "users_table"
    phone_number: Mapped[str] = mapped_column(String, nullable=False)
    def __repr__(self):
        return f"User={self.full_name}   email={self.email} "


class UserExtension(Base):
    """ User Extension ORM model:
    -- This model extends class User and helps to store additional data fields .
    Args:
        Base (SQLAlchemy Base class): 
    Returns:
        UserExtention ORM Model:
    """
    __tablename__ = 'user_extension'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[UUID_ID] = mapped_column(ForeignKey("users_table.id"))
    position: Mapped[Optional[str]] = mapped_column(String)
    company: Mapped[UUID_ID] = mapped_column(ForeignKey("company_table.id"))
    options: Mapped[Optional[dict]] = mapped_column(JSON)
    birth_date: Mapped[date.fromisoformat] = mapped_column(Date)
    avatar: Mapped[Optional[bytes]] = mapped_column(LargeBinary)
    full_name: Mapped[str] = mapped_column(String)
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
    director: Mapped[Optional[UUID_ID]] = mapped_column(ForeignKey("users_table.id")) # How many directors may run business ??
    email: Mapped[Optional[str]] = mapped_column(String)
    address: Mapped[Optional[str]] = mapped_column(String)
    location: Mapped[Optional[str]] = mapped_column(String)
    options: Mapped[Optional[dict]] = mapped_column(JSON)
    credentials: Mapped[Optional[dict]] = mapped_column(JSON)
    company_logo: Mapped[Optional[bytes]] = mapped_column(LargeBinary)
    def __repr__(self):
        return f"Company Name={self.user_id} company_id={self.id}"