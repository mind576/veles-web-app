
from fastapi import APIRouter, Depends, HTTPException, Response
from starlette.responses import JSONResponse
from src.users import fastapi_users
from src.users import *
from sqlalchemy.exc import SQLAlchemyError
from src.models import User, Employee
from starlette import status
from src.users import current_active_user,current_superuser
from src.db import AsyncSession, get_async_session
from src.schemas import EmployeeRead, EmployeeUpdate,EmployeeCreate
import uuid
from sqlalchemy import select, update, insert, text
from starlette import status
from datetime import  datetime



ext_router = APIRouter(prefix="/employee",
)

@ext_router.post("/add",tags=['Employee Method'])
async def create_employee(
    employee: EmployeeCreate,
    user: User = Depends(current_active_user), # T E M P O R A R Y implementation are current_userlater it should do superuser
    # user: User = Depends(current_superuser)     
    session: AsyncSession = Depends(get_async_session),
    ):
    """
    ### Async method that creates Employee to database:\n
    Employee are linked with User by ForeinKey parameter so it extends
    basic User Model and gives additional fields to User.\n
    Args:\n
        user - Depends(current_superuser).\n
        * only superuser may create employee
        session - (AsyncSession) Depends(get_async_session).\n
        employee - Employee schema\n
    #### *Only superuser my change and create Employee    
    ##### Please read schema for understanding JSON schema
    """
    try:
        if isinstance(employee.position,str):
            new_employee = Employee(
            user_id=user.id,
            position=employee.position,
            obligations=employee.obligations
            )
            session.add(new_employee)
            await session.commit()
            return JSONResponse(status_code=status.HTTP_201_CREATED,content={"details":"created"})    
    except SQLAlchemyError as e:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))    



@ext_router.put("/update/{user_id}",tags=['Update Employee Method'])
async def update_emloyee(
    user_id: int,
    employee: EmployeeUpdate,
    user: User = Depends(current_active_user), # T E M P O R A R Y - only superuser may update Employee
    # user: User = Depends(current_superuser)
    session: AsyncSession = Depends(get_async_session),
    ):
    """
   ### Async method that updates Employee :\n
    Employee are linked with User by ForeinKey parameter so extends
    basic User Model and gives additional fields to User.\n
    Args:\n
        user_id: int of linked User that you want to update.\n
        session - (AsyncSession) Depends(get_async_session).\n
        employee - EmployeeUpdate schema\n
    #### *Only superuser my change and create Employee    
    ##### Please read schema for understanding JSON schema
    """
    try:
        if user:
            statement = update(
            Employee).where(
                Employee.user_id == user_id).values(
                    position=employee.position,
                    obligations=employee.obligations,
                )
            await session.execute(statement)
            await session.commit()
    except SQLAlchemyError :                            # later will do e  to logger
        raise HTTPException(status_code=404,detail=status.HTTP_404_NOT_FOUND)
    return Response(status_code=201)



# Unfinished --- WORK HERE !!!
# @ext_router.get("/get")
# async def get_employee_id(
#     user_id: int,
#     user: User = Depends(current_active_user),
#     session: AsyncSession = Depends(get_async_session)
#     ):
#     if user_id:
#         try:
#             statement = select(Employee).where(Employee.user_id == user_id)
#             retrieved_employee = await session.execute(statement=statement)
#             if retrieved_employee:
#                 return retrieved_employee
#         except SQLAlchemyError:
#             raise HTTPException(status_code=404,detail=status.HTTP_404_NOT_FOUND)
