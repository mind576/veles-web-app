from fastapi import Depends, FastAPI
from src.models import User, Employee
from src.db import create_db_and_tables
from src.schemas import UserCreate, UserRead, UserUpdate
from src.users import auth_backend, current_active_user, fastapi_users
from src.employee import ext_router as user_extender_router
from src.cmp import cmp_router as company_router
from settings import config
from src.db import Base 
from src.db import engine

# P R E S E N T A T I O N    D A T A
contact_dict = dict(name=config['CONTACT_NAME'],
                    email=config['CONTACT_EMAIL'],
                                  )
app = FastAPI(title=config['API_TITLE'],description=config['API_DESCRIPTION'],contact=contact_dict)

# User Extender Router - Imported from module extender.py
app.include_router(
    user_extender_router,tags=['UserExtension Methods']
    )
# company Router - cmp.py
app.include_router(
    company_router,tags=['Company Methods ']
    )

# users backend
app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["Login / Logout Methods"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Register User Methods"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["Reset Password Methods"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["Veryfy Methods"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["User CRUD Methods"],
)


@app.get("/authenticated-route",tags=['Hello World Method'])
async def authenticated_route(command:str = None):
    """Dev usage cludge"""
    if command:
        match command:
            case "create_all":
                async with engine.begin() as conn:
                    await conn.run_sync(Base.metadata.create_all)
            case "drop_all":
                async with engine.begin() as conn:
                    await conn.run_sync(Base.metadata.drop_all)
                    
    return {"message": f"Hello Word!" }


# import importlib
# @app.on_event("startup")
# async def on_startup():
#     async with engine.begin() as conn:
#         # await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)