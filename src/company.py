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


cmp_router = APIRouter(prefix="/company",
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
    Company - are created by registred ***user***, user who creates company is superuser and admin for particular company  .\n
    Args:\n
        user - Depends(current_superuser).\n
        session - (AsyncSession) Depends(get_async_session).\n
        company - CompanyCreate schema\n
    #### *Only director my change Company data.
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
                OGRN = company.OGRN,                                        # NO SOLVED PUT DATA
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




@cmp_router.patch("/update/{company_id}",tags=['Update Company Method'])
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
                    OGRN = company.OGRN,                                        # Temporary how
                    BIK = company.BIK,
                    bank_name = company.bank_name,
                    bank_address= company.bank_address,
                    corr_account = company.corr_account,
                )
            await session.execute(statement)
            await session.commit()
    except SQLAlchemyError as e:                            # <<<< later will do e  to logger
        raise HTTPException(status_code=404,detail=status.HTTP_404_NOT_FOUND)
    return Response(status_code=201)



# DELETE COMPANY

@cmp_router.delete("/delete/{company_id}",tags=['Delete Company Method'])
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
            if del_company.director == user.id:
                await session.delete(del_company)
                await session.commit()
    except SQLAlchemyError as e:                            # <<<< later will do e  to logger
        raise HTTPException(status_code=404,detail=status.HTTP_404_NOT_FOUND)
    return Response(status_code=201)

