from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from settings import *
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy import String, Date, ForeignKey,JSON
from datetime import date



Base: DeclarativeMeta = declarative_base()


class User(SQLAlchemyBaseUserTableUUID, Base):
    """
    User table.
    """
    __tablename__ = "users_table"
    phone_number: Mapped[str] = mapped_column(String, nullable=False)
    registred_date: Mapped[date.fromisoformat] = mapped_column(Date)
    def __repr__(self):
        return f"User={self.name}   email={self.email} "


class UserExtension(Base):
    """ User Extention model which has obvious fields:
    -- This model extends class User and stores additional fields data.
    Args:
        Base (SQLAlchemy Base class): 
    Returns:
        UserExtention ORM Model:
    """
    __tablename__ = 'user_extension'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users_table.id"))
    position: Mapped[Optional[str]] = mapped_column(String)
    company: Mapped[Optional[str]] = mapped_column(String)
    options: Mapped[Optional[dict]] = mapped_column(JSON)
    def __repr__(self):
        return f"User_id={self.user_id}   email={self.company} "