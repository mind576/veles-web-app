from dotenv import dotenv_values
import pathlib
import os
import time

# ROOT DIRECTORY OF THE PROJECT
root_dir = pathlib.Path(__file__).parent.resolve()

# DOTENV FILE
config = dotenv_values(f"{root_dir}/.env")

# # # #      - = TEMP KLUDGE = -    DEVELOPMENT USAGE ONLY (костыль для разработки)

if config['POSTGRES_DOCKER_BUILD'] == 'True':   #### This param true/false  docker build
    PG_HOST = config["POSTGRES_HOST_DOCKER"]
elif config['POSTGRES_DOCKER_BUILD'] == 'False':
    PG_DOCKER_RUN_DEV_MODE = config['DEV_DOKER_POSTGRES_CMD']
    PG_HOST = config["POSTGRES_HOST_LOCAL"]  
    # N O T I C E   ---    While building app with docker-compose this part running "docker run postgres container"
    # os.system(PG_DOCKER_RUN_DEV_MODE)            
    # time.sleep(10)
    # os.system(f'echo "Service is run on {PG_HOST}"')


PG_PASS = config['POSTGRES_PASSWORD']
PG_USER = config['POSTGRES_USER']
PG_DB_NAME = config['POSTGRES_DB']
SECRET_TOKEN =config['SECRET_TOKEN']
PG_PORT=config['POSTGRES_PORT']
JWT_TOKEN_LIFETIME = config['JWT_TOKEN_LIFETIME']
# REDIS cache
CACHE_EXP = config['CACHE_EXP']
LOCAL_REDIS_URL = config['LOCAL_REDIS_URL']
CACHE_PREFIX = config['CACHE_PREFIX']


# uvicorn src.app:app --reload
