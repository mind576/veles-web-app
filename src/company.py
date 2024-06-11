from fastapi import APIRouter, Depends, HTTPException, Response
from starlette.responses import JSONResponse
from src.users import *
from src.models import Company
from fastapi import APIRouter, Depends, HTTPException
from src.users import fastapi_users
from src.users import *
from sqlalchemy.exc import SQLAlchemyError
from src.models import User, Employee
from starlette import status
from src.users import current_active_user ,current_superuser
from src.schemas import CompanyCreate, CompanyRead, CompanyUpdate
from src.db import AsyncSession, get_async_session
from sqlalchemy import select, update
from starlette import status


current_user = fastapi_users.current_user(active=True)


cmp_router = APIRouter(prefix="/business",
    responses={404: {"description": "Not found"}},
)

# @cmp_router.post("/add",tags=['Create Company Method'])
# async def create_company(user: User = Depends(current_active_user)):
#     """
#     Company - ORM model that represents company item.
#     By adding this tem to database you've creating company. The User which created Company are admin for company and it's processes.
#     The only this User who created company may manage processes, add workers to company and initiate Constructions.
#     """
#     return {"message": f"Hello {user.email}!"}


# @cmp_router.get("/get")
# async def get_copmany(user: User = Depends(current_user)):
#     return user



@cmp_router.post("/add",tags=['Company Create Method'])
async def create_company(
    company: CompanyCreate,
    user: User = Depends(current_active_user), # T E M P O R A R Y implementation are current_userlater it should do superuser
    # user: User = Depends(current_superuser)     
    session: AsyncSession = Depends(get_async_session),
    ):
    """
    ### Async method that creates Company item:\n
    Employee are linked with User by ForeinKey parameter so it extends
    basic User Model and gives additional fields to User during it's work on a position.\n
    Args:\n
        user - Depends(current_superuser).\n
        * only superuser may create employee
        session - (AsyncSession) Depends(get_async_session).\n
        employee - Employee schema\n
    #### *Only superuser my change and create Employee    
    ##### Please read schema for understanding JSON schema
    """
    try:
        if isinstance(company,CompanyCreate):
            new_company = Company(
                name = company.name,
                director = user.id,
                phone = company.phone,
                email = company.email,
                address = company.address,
                location = company.location,
                info = company.info,
                type = company.type,
                name_legal = company.name_legal,
                INN = company.INN,
                KPP = company.KPP,
                OGRN = company.OGRN,
                BIK = company.BIK,
                bank_name = company.bank_name,
                bank_address= company.bank_address,
                corr_account = company.corr_account,   
            )
            session.add(new_company)
            await session.commit()
            return JSONResponse(status_code=status.HTTP_201_CREATED,content={"detail":"created"})    
    except SQLAlchemyError as e:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))    


    # id: Mapped[int] = mapped_column(Integer,primary_key=True)
    # name: Mapped[Optional[str]] = mapped_column(String)
    # director: Mapped[Optional[int]] = mapped_column(ForeignKey("users_table.id"),nullable=True)
    # phone: Mapped[str] = mapped_column(String, nullable=False)
    # email: Mapped[Optional[str]] = mapped_column(String)
    # address: Mapped[Optional[str]] = mapped_column(String)
    # location: Mapped[Optional[str]] = mapped_column(String)
    # info: Mapped[Optional[str]] = mapped_column(String)
    # type: Mapped[Optional[str]] = mapped_column(String)
    # name_legal: Mapped[Optional[str]] = mapped_column(String)
    # INN: Mapped[Optional[str]] = mapped_column(String)
    # KPP: Mapped[Optional[str]] = mapped_column(String)
    # OGRN: Mapped[Optional[str]] = mapped_column(String)
    # OKPO: Mapped[Optional[str]] = mapped_column(String)
    # BIK: Mapped[Optional[str]] = mapped_column(String)
    # bank_name: Mapped[Optional[str]] = mapped_column(String)
    # bank_address: Mapped[Optional[str]] = mapped_column(String)
    # corr_account: Mapped[Optional[str]] = mapped_column(String)








# @cmp_router.patch("/update/{user_id}",tags=['Update Employee Method'])
# async def update_emloyee(
#     user_id: int,
#     employee: EmployeeUpdate,
#     user: User = Depends(current_active_user), # T E M P O R A R Y - only superuser may update Employee
#     # user: User = Depends(current_superuser)
#     session: AsyncSession = Depends(get_async_session),
#     ):
#     """
#    ### Async method that updates/patches Employee item :\n
#     Employee are linked with User by ForeinKey parameter so extends
#     basic User Model and gives additional fields to User.\n
#     Args:\n
#         user_id: int of linked User that you want to update.\n
#         session - (AsyncSession) Depends(get_async_session).\n
#         employee - EmployeeUpdate schema\n
#     #### *Only superuser my change and create Employee    
#     ##### Please read schema for understanding JSON schema
#     """
#     try:
#         if user:
#             statement = update(
#             Employee).where(
#                 Employee.user_id == user_id).values(
#                     position=employee.position,
#                     obligations=employee.obligations,
#                 )
#             await session.execute(statement)
#             await session.commit()
#     except SQLAlchemyError as e:                            # <<<< later will do e  to logger
#         raise HTTPException(status_code=404,detail=status.HTTP_404_NOT_FOUND)
#     return Response(status_code=201)





# @cmp_router.get("/get/{user_id}",response_model=EmployeeRead,tags=['Get Employee item by user_id'])
# async def get_employee_id(
#     user_id: int,
#     user: User = Depends(current_active_user),
#     # user: User = Depends(current_superuser)
#     session: AsyncSession = Depends(get_async_session)
#     ):
#     """
#    ### Async method that retrieves Employee by user_id int param :\n
#     Employee are linked with User by ForeinKey parameter so extends
#     basic User Model and gives additional fields to User.\n
#     Args:\n
#         user_id: int of linked User that you want to retrieve.\n
#         session - (AsyncSession) Depends(get_async_session).\n
#         employee - EmployeeUpdate schema\n
#     ##### Please read schema for understanding JSON schema
#     """
#     if user_id:
#         try:
#             statement = select(Employee).where(Employee.user_id == user_id)
#             result = await session.execute(statement=statement)
#             retrieved = result.scalar() # retrieved employee item
#             if retrieved:
#                 return retrieved # Here is pure scalar object that parses response_model=EmployeeRead
#             else:
#                 return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,content={"detail":"item not found"})
            
#         except SQLAlchemyError as e:                                            # <<<< later will do e  to logger
#             raise HTTPException(status_code=404,detail=status.HTTP_404_NOT_FOUND)