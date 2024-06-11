
from fastapi import APIRouter, Depends, HTTPException
from src.users import fastapi_users
from src.users import *
from src.models import User, Employee
from starlette import status
from src.users import current_active_user ,current_superuser


current_user = fastapi_users.current_user(active=True)


cmp_router = APIRouter(prefix="/business",
    responses={404: {"description": "Not found"}},
)

@cmp_router.post("/add",tags=['Create Company Method'])
async def create_company(user: User = Depends(current_active_user)):
    """
    Company - ORM model that represents company item.
    By adding this tem to database you've creating company. The User which created Company are admin for company and it's processes.
    The only this User who created company may manage processes, add workers to company and initiate Constructions.
    """
    return {"message": f"Hello {user.email}!"}


@cmp_router.get("/get")
async def get_copmany(user: User = Depends(current_user)):
    return user