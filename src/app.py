from fastapi import  FastAPI
from src.schemas import UserCreate, UserRead, UserUpdate
from src.users import auth_backend,  fastapi_users
from src.employee import ext_router as user_extender_router
from src.company import cmp_router as company_router
from settings import config
from src.db import Base 
from src.db import engine


tags_meta = [
    {
        "name": "Users",
        "description": "UMA - User management Authentication methods flow. Registration, Authentication, Reset password, etc.",
    },
    {
        "name": "Company",
        "description": " Company ORM model methods that represents company Item with data fields."
    },
    {
        "name": "Employee",
        "description": "Employee ORM that extends User model so it gives additional data to user as employee. Logically user may change the employment so someone may substitute user on particular position.When particular user is unemployed he has no Employee table...\nThis table are used by user which works in the company on concrete position."
    },
]

# OpenAPI  - P R E S E N T A T I O N    D A T A
contact_dict = dict(name=config['CONTACT_NAME'],
                    email=config['CONTACT_EMAIL'],
                                  )
app = FastAPI(title=config['API_TITLE'],description=config['API_DESCRIPTION'],contact=contact_dict,openapi_tags=tags_meta)

# Employee Router - Imported from module employee.py
app.include_router(
    user_extender_router,tags=['Employee Methods']
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