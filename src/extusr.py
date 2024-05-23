
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
from sqlalchemy import select, update,insert
from starlette import status
from datetime import  datetime



ext_router = APIRouter(prefix="/ext",
)

@ext_router.post("/add",tags=['Create UserExtension Method'])
async def create_user_extension(
    ext: UserExtCreate,
    user: User = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
    ):
    """
    ### Async method that creates UserExtention item to database:\n
    UserExtention are linked with User by ForeinKey parameter so it extends
    basic User Model and gives additional fields to User.\n
   
    
    Args:\n
        active user - Depends(current_active_user).\n
        session - (AsyncSession) Depends(get_async_session).\n
        extention - UserExtCreate shema\n
        
    #### Please read schema for understanding JSON schema
    """
    try:
        statement = (insert(UserExtension).values(
            user_id=user.id, 
            profession=f'{ext.profession}',
            company=f'{ext.company}',
            options_dict=f'{ext.options_dict}',
            birth_date=f'{ext.birth_date}',
            avatar=f'{ext.vatar}'
            ))
        session.execute(statement=statement)
        await session.commit()
        return Response(status_code=201,detail=status.HTTP_201_CREATED)
    except SQLAlchemyError as e:
        return HTTPException(status_code=400,detail=status.HTTP_400_BAD_REQUEST)



@ext_router.put("/update/{user_id}",tags=['Update UserExtension Method'])
async def update_user_extension(
    user_id: uuid.UUID,
    ext: UserExtUpdate,
    user: User = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
    ):
    """
   ### Async method that puts or updates UserExtention item to database:\n
    UserExtention are linked with User by ForeinKey parameter so extends
    basic User Model and gives additional fields to User.\n
   

    Args:\n
        user_id: uuid of User that you want to retrieve.\n
        session - (AsyncSession) Depends(get_async_session).\n
        extention - UserExtUpdate shema\n
        
        
    #### Please read schema for understanding JSON schema
    """
    try:

        statement = update(
            UserExtension).where(
                UserExtension.id == user_id).values(
                    profession=f"{ext.profession}",
                    options_dict=f"'{ext.options_dict}'",
                    birth_date=f"{ext.birth_date}",
                    avatar=f"{ext.avatar}",

                )
        session.execute(statement)
        await session.commit()
    except SQLAlchemyError as e:                            # later will do e  to logger
        raise HTTPException(status_code=404,detail=status.HTTP_404_NOT_FOUND)
    return Response(status_code=201, detail=status.HTTP_201_CREATED)




@ext_router.get("/get")
async def get_extension_uuiid(
    user_uuid: uuid.UUID,
    user: User = Depends(current_active_user)):
    return user