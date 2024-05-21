
from fastapi import APIRouter, Depends, HTTPException, Response
from src.users import fastapi_users
from src.users import *
from sqlalchemy.exc import SQLAlchemyError
from src.models import User, UserExtension
from starlette import status
from src.users import current_active_user
from src.db import AsyncSession, get_user_extension_db
from src.schemas import UserExtCreate, UserExtRead, UserUpdate
import uuid



ext_router = APIRouter(prefix="/ext",
    responses={404: {"description": "Not found"}},
)

@ext_router.post("/add",tags=['Create UserExtension Method'])
async def create_user_extension(
    ext: UserExtCreate,
    user: User = Depends(current_active_user),
    session: AsyncSession = Depends(get_user_extension_db),
    ):
    """
    Async method that creates and puts UserExtention item to database:
    UserExtention are linked with User by ForeinKey parameter so extends
    basic User Model and gives additional fields to User.
    Additional fields has needed data for disclosure User's options and information about User credentials.

    Args:
        active user (UserExtention, optional): _description_. Defaults to Depends(current_active_user).
        session (AsyncSession, optional): _description_. Defaults to Depends(get_async_session).
        extention (UserExtension, optional): _description_. Defaults to Depends(current_user).

    Returns:
        _type_: _description_
    """
    try:
        new_extention = UserExtension(
            user_id = current_active_user.id,
            position = ext.position,
            company= ext.position,
            options = ext.options,
            birth_date = ext.birth_date,
            avatar = ext.avatar,
            full_name = ext.full_name
        ) 
        session.add(new_extention)
        await session.commit()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400,detail=str(e))
    return Response(status_code=201, detail="Created")



@ext_router.get("/get")
async def extender_test(user: User = Depends(current_active_user)):
    return user