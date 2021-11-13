# FASTAPI INTRODUCTION

**FastAPI, PostgreSQL, Async SQLAlchemy, Async requests with AIOHTTP**

Video code on youtube: https://www.youtube.com/watch?v=1CZZAhwqyco

## Dependecies
* Docker
* Docker-compse
* Python >= 3.6
* Pipenv

## How to run
Add project path at `PYTHONPATH` variable in `.env` file.

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

Populate database
```shell
python populate.py
```

Start application
```shell
uvicorn main:app --port 8080
```

## Compare sync and async views
There are two versions of assets/day_summary endpoint, so you can compare both performance.
