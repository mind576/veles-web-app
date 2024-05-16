from dotenv import dotenv_values
import pathlib
import os
import time

# ROOT DIRECTORY OF THE PROJECT
root_dir = pathlib.Path(__file__).parent.resolve()

# DOTENV FILE
config = dotenv_values(f"{root_dir}/.env")

# When it's building it feeds from .env  docker url
if config['POSTGRES_DOCKER_BUILD'] == 'True':
    PG_HOST = config["POSTGRES_HOST_DOCKER"]
elif config['POSTGRES_DOCKER_BUILD'] == 'False':
    PG_DOCKER_RUN_DEV_MODE = config['DEV_DOKER_POSTGRES_CMD']
    PG_HOST = config["POSTGRES_HOST_LOCAL"]
    
    # If you prefer on the start this cmd will execute - run docker container with postgres instance
    os.system(PG_DOCKER_RUN_DEV_MODE)             # DEV_DOKER_POSTGRES_CMD='docker run --name db_postgres  -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -d postgres:latest'

    time.sleep(10)
    os.system(f'echo "Service is run on {PG_HOST}"')


PG_PASS = config['POSTGRES_PASSWORD']
PG_USER = config['POSTGRES_USER']
PG_DB_NAME = config['POSTGRES_DB']
SECRET_TOKEN =config['SECRET_TOKEN']
PG_PORT=config['POSTGRES_PORT']



# uvicorn src.app:app --reload