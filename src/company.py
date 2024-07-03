from fastapi import APIRouter, Depends, HTTPException, Response, Request
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
from fastapi_cache.decorator import cache as cache_decorator
from fastapi_redis_cache import cache_one_minute
from src.custom_responses import *
current_user = fastapi_users.current_user(active=True)


cmp_router = APIRouter(prefix="/company",
    responses=ROUTER_API_RESPONSES_OPEN_API
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



@cmp_router.post("/add")
async def create_company(
    company: CompanyCreate,
    user: User = Depends(current_active_user), # T E M P O R A R Y implementation are current_userlater it should do superuser
    # user: User = Depends(current_superuser)     
    session: AsyncSession = Depends(get_async_session),
    ):
    """
    ### Async method that creates Company item:\n
    Company - are created by registred ***user***, user who creates company is superuser and admin for particular company  .\n
    Args:\n
        user - Depends(current_superuser).\n
        session - (AsyncSession) Depends(get_async_session).\n
        company - CompanyCreate schema\n
    #### *Only director my change Company data.
    ##### Please read schema for understanding JSON schema
    """
    try:
        if isinstance(company,CompanyCreate): # temporary check
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
                OKPO = company.OKPO,                                        # NO SOLVED PUT DATA
                BIK = company.BIK,
                bank_name = company.bank_name,
                bank_address= company.bank_address,
                corr_account = company.corr_account,   
            )
            session.add(new_company)
            await session.commit()
            return JSONResponse(status_code=status.HTTP_201_CREATED,content={"detail":"created"})    
    except SQLAlchemyError as e:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e._message))    




@cmp_router.put("/update/{company_id}")
async def update_company(
    company_id: int,
    company: CompanyUpdate,
    user: User = Depends(current_active_user), # T E M P O R A R Y - only superuser may update Employee
    # user: User = Depends(current_superuser)
    session: AsyncSession = Depends(get_async_session),
    ):
    """
   ### Async method that updates/patches Company item :\n
    Company - are created by registred ***user***, user who creates company is superuser and admin for particular company  .\n
    Args:\n
        user - Depends(current_superuser).\n
        session - (AsyncSession) Depends(get_async_session).\n
        company - CompanyCreate schema\n
    #### *Only director my change Compay data.  
    ##### Please read schema for understanding JSON schema
    """
    try:
        if user:
# id: Mapped[int] = mapped_column(Integer,primary_key=True)
#     name: Mapped[str] = mapped_column(String,unique=True)
#     director: Mapped[int] = mapped_column(ForeignKey("user_table.id"),nullable=True)
#     phone: Mapped[str] = mapped_column(String, nullable=False)
#     email: Mapped[str] = mapped_column(String)
#     address: Mapped[str] = mapped_column(String)
#     location: Mapped[str] = mapped_column(String)
#     info: Mapped[str] = mapped_column(String)
#     type: Mapped[str] = mapped_column(String)
#     name_legal: Mapped[str] = mapped_column(String)
#     INN: Mapped[str] = mapped_column(String, unique=True)
#     KPP: Mapped[str] = mapped_column(String)
#     OGRN: Mapped[str] = mapped_column(String,unique=True)
#     OKPO: Mapped[str] = mapped_column(String,nullable=True) #<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     BIK: Mapped[str] = mapped_column(String)
#     bank_name: Mapped[str] = mapped_column(String)
#     bank_address: Mapped[str] = mapped_column(String)
#     corr_account: Mapped[str] = mapped_column(String)
#     employees: Mapped[List["Employee"]] = relationship(back_populates="company")

            statement = update(
            Company).where(
                Company.id == company_id).values(
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
                    OKPO = company.OKPO,                                                                                # Temporary how
                    BIK = company.BIK,
                    bank_name = company.bank_name,
                    bank_address= company.bank_address,
                    corr_account = company.corr_account,
                )
            await session.execute(statement)
            await session.commit()
    except SQLAlchemyError as e:                            # <<<< later will do e  to logger
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e._message))
    # return Response(status_code=201)



# DELETE COMPANY

@cmp_router.delete("/delete/{company_id}")
async def delete_company(
    company_id: int,
    user: User = Depends(current_active_user), # T E M P O R A R Y - only superuser may update Employee
    # user: User = Depends(current_superuser)
    session: AsyncSession = Depends(get_async_session),
    ):
    """
   ### Async method that deletes Company item :\n
    Company - are created by registred ***user***, user who creates company is superuser and admin for particular company  .\n
    Args:\n
        user - Depends(current_superuser).\n
        session - (AsyncSession) Depends(get_async_session).\n
        company - Company ORM\n
    #### *Only director my change Compay data.  
    ##### Please read schema for understanding JSON schema
    """
    try:
        if user and company_id:
            del_company = await session.get(Company, company_id)
            if del_company:
                await session.delete(del_company)
                await session.commit()
            elif not del_company:
                return Response(status_code=status.HTTP_404_NOT_FOUND,content="not exist",background=print(str(del_company))) # Logger binding with background param
                
    except SQLAlchemyError as e:                            # <<<< later will do e  to logger
        raise HTTPException(status_code=404,detail=str(e._message))
    return Response(status_code=status.HTTP_200_OK)


@cmp_router.get("/get/{company_id}") #,response_model=CompanyRead)
async def get_company_id(
    company_id: int,
    user: User = Depends(current_active_user), # T E M P O R A R Y - only superuser may update Employee
    # user: User = Depends(current_superuser)
    session: AsyncSession = Depends(get_async_session),
    ):
    """
   ### Async method that gets Company item by id :\n
    Company - are created by registred ***user***, user who creates company is superuser and admin for particular company  .\n
    Args:\n
        user - Depends(current_superuser).\n
        session - (AsyncSession) Depends(get_async_session).\n
        company - Company ORM\n
    #### *Only director my change Compay data.  
    ##### Please read schema for understanding JSON schema
    """
    try:
        if user and company_id:
            company = await session.get(Company, company_id)
            if company:
                return company
    except SQLAlchemyError as e:                            # <<<< later will do e  to logger
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(e._message))
    return Response(status_code=status.HTTP_404_NOT_FOUND)


# Response.background = logger




