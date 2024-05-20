
from fastapi import APIRouter, Depends, HTTPException
from src.users import fastapi_users
from src.users import *
from src.models import User, UserExtension
from starlette import status
from src.users import current_active_user


current_user = fastapi_users.current_user(active=True)


router = APIRouter(prefix="/extuser",
    responses={404: {"description": "Not found"}},
)

@router.post("/add",tags=['Create UserExtention Method'])
async def create_user_extender(user: User = Depends(current_active_user)):
    
    return {"message": f"Hello {user.email}!"}


@router.get("/get")
async def extender_test(user: User = Depends(current_user)):
    return user