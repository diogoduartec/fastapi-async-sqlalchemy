# FASTAPI INTRODUCTION
**Fastapi, Postgres, Async Sqlalchemy, Async requests with Aiohttp**

## Dependecies
* Docker
* Docker-compse
* Python >= 3.6
* Pipenv

## How to run
Start **postgres** database and **pgadmin**
```shell
docker-compose up -d
```

Start environment
```shell
pipenv shell
```

Install python dependencies
```shell
pipenv install
```

Start application
```shell
uvicorn main:app --port 8080
```
