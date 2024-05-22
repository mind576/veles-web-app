
from fastapi import APIRouter, Depends, HTTPException, Response
from src.users import fastapi_users
from src.users import *
from sqlalchemy.exc import SQLAlchemyError
from src.models import User, UserExtension
from starlette import status
from src.users import current_active_user
from src.db import AsyncSession, get_async_session
from src.schemas import UserExtCreate, UserExtRead, UserUpdate,UserExtUpdate
import uuid
from sqlalchemy import select, update
from starlette import status
    



ext_router = APIRouter(prefix="/ext",
)

@ext_router.post("/add",tags=['Create UserExtension Method'])
async def create_user_extension(
    ext: UserExtCreate,
    user: User = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
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
        return HTTPException(status_code=400,detail=status.HTTP_400_BAD_REQUEST)
    return Response(status_code=201, detail=status.HTTP_201_CREATED)


@ext_router.put("/update/{user_id}",tags=['Update UserExtension Method'])
async def update_user_extension(
    user_id: uuid.UUID,
    ext: UserExtUpdate,
    user: User = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
    ):
    """
    
    Args:
        active user (UserExtention, optional): _description_. Defaults to Depends(current_active_user).
        session (AsyncSession, optional): _description_. Defaults to Depends(get_async_session).
        extention (UserExtension, optional): _description_. Defaults to Depends(current_user).

    Returns:
        _type_: _description_
    """
    try:
        # retrieved instance by user_id
        # retr_statement = select(UserExtension).where(UserExtension.id == user_id)
        # retr_results = await session.execute(retr_statement)
        # retr_instance = retr_results.scalars().first()
        # _params = [
        #     ext.position,
        #     ext.options,
        #     ext.birth_date,
        #     ext.avatar,
        #     ext.full_name
        #     ]
        # _values = [x for x in _params if x != None ]
        # C H E C K  It
        statement = update(
            UserExtension).where(
                UserExtension.id == user_id).values(
                    position=f"{ext.position}",
                    options=f"{ext.options}",
                    birth_date=f"{ext.birth_date}",
                    avatar=f"{ext.avatar}",
                    full_name=f"{ext.full_name}",
                )
        session.execute(statement)
        await session.commit()
            
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400,detail=status.HTTP_400_BAD_REQUEST)
    return Response(status_code=201, detail=status.HTTP_201_CREATED)




@ext_router.get("/get")
async def get_extension_uuiid(
    user_uuid: uuid.UUID,
    user: User = Depends(current_active_user)):
    return user