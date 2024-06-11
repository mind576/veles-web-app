
from fastapi import APIRouter, Depends, HTTPException
from src.users import fastapi_users
from src.users import *
from src.models import User, Employee
from starlette import status
from src.users import current_active_user


current_user = fastapi_users.current_user(active=True)


cmp_router = APIRouter(prefix="/business",
    responses={404: {"description": "Not found"}},
)

@cmp_router.post("/add",tags=['Create Company Method'])
async def create_company(user: User = Depends(current_active_user)):
    
    return {"message": f"Hello {user.email}!"}


@cmp_router.get("/get")
async def get_copmany(user: User = Depends(current_user)):
    return user