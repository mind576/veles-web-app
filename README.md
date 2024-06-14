** Users management **

> [!NOTE]
> Приложение для - Auth User Management ( В процессе разработки ).


### Auth User App - Микросервис 

```.env

POSTGRES_DOCKER_BUILD='False'
POSTGRES_HOST_DOCKER=pgbase
POSTGRES_HOST_LOCAL=localhost
POSTGRES_PASSWORD=secret123
POSTGRES_USER=postgres
POSTGRES_DB=postgres
SECRET_TOKEN=secret
POSTGRES_PORT=5432
DEV_DOKER_POSTGRES_CMD='docker run -it --name pgbase -e POSTGRES_PASSWORD=secret123 -p 5432:5432 -d postgres:latest'
JWT_TOKEN_LIFETIME=3600

CONTACT_NAME='Ivan Goncharov'
CONTACT_EMAIL='ivan.stereotekk@gmail.com'
API_TITLE='UMA web application'
API_DESCRIPTION='VELES company user management REST methods'

```

