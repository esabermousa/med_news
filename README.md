# 

## Solution & Desgin

### Solution
> 

### Technologies
- PostgresDB 10
- python 3.6
- Flask Web Framework
- Flask-sqlalchemy
- nginx
- Docker
- Docker-compose
- JWT
- Pytest

## Deploymet
```bash
# install Docker and Docker-compose
You have to have installed [docker](https://www.docker.com/) & [docker-compose](https://docs.docker.com/compose/install/) in other to make it work.

# build and run containers
docker-compose up -d

# SSH into the container
docker-compose exec flask /bin/bash

# Create DB schema and seed feeds
python manage.py recreate_db
