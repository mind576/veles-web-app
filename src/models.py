from typing import Optional,List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from fastapi_users.db import SQLAlchemyBaseUserTable
from settings import *
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy import String, Date, ForeignKey,LargeBinary,Integer,Boolean, DateTime
from datetime import date
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
import uuid


Base: DeclarativeMeta = declarative_base()

UUID_ID = uuid.UUID


class User(SQLAlchemyBaseUserTable[int], Base):
    """
    User table with obvious and visible fields and options.
    
    """
    __tablename__ = 'user_table'
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    full_name: Mapped[str] = mapped_column(String,nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True,nullable=False)
    phone: Mapped[str] = mapped_column(String,unique=True, nullable=False)
    picture: Mapped[str] = mapped_column(String)
    birth_date: Mapped[date] = mapped_column(Date,nullable=True)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)

    def __repr__(self):
        return f" id={self.id} name= {self.full_name} "



class Employee(Base):
    """ Employee ORM that extends User model so it gives additional data to user as employee. Logically \n
    user may change the employment so someone may substitute user on particular position.\n
    Exact that time when user is employeed this table gives info about position and obligations.\n
    When particular user is unemployed he has no Employee table...\n
    This table are used by user which works in the company on concrete position.
    #### * I recon this table will get some new fields later ---

    """
    __tablename__ = 'employee_table'
    id: Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"),unique=True)
    position: Mapped[str] = mapped_column(String,nullable=True)
    obligations: Mapped[str] = mapped_column(String,nullable=True)
    company_id: Mapped[int] = mapped_column(ForeignKey("company_table.id"),nullable=True)
    company: Mapped["Company"] = relationship(back_populates="employees")
    
    def __repr__(self):
        return f"id={self.user_id}   position={self.position}  company={self.company}"
    
    
    
class Company(Base):
    """ Company ORM model:
    -- This model helps to store Company table data fields .
    Args:
        Base (SQLAlchemy Base class): 
    Returns:
        Company ORM Model:
    """
    __tablename__ = 'company_table'
    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    name: Mapped[str] = mapped_column(String,unique=True)
    director: Mapped[int] = mapped_column(ForeignKey("user_table.id"),nullable=True)
    phone: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String)
    address: Mapped[str] = mapped_column(String)
    location: Mapped[str] = mapped_column(String)
    info: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)
    name_legal: Mapped[str] = mapped_column(String)
    INN: Mapped[str] = mapped_column(String, unique=True)
    KPP: Mapped[str] = mapped_column(String)
    OGRN: Mapped[str] = mapped_column(String,unique=True)
    OKPO: Mapped[str] = mapped_column(String,nullable=True) #<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    BIK: Mapped[str] = mapped_column(String)
    bank_name: Mapped[str] = mapped_column(String)
    bank_address: Mapped[str] = mapped_column(String)
    corr_account: Mapped[str] = mapped_column(String)
    employees: Mapped[List["Employee"]] = relationship(back_populates="company")

    def __repr__(self):
        return f"Company Name={self.name} company_id={self.id} legal={self.name_legal}"