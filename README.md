# Tricago Full stack task

## Solution & Desgin

### Solution
> i assume that all tasks related with each other, so i'll use postgres as DB to
store all feeds details to allow me to retrive & update them whenever i need.
also there are 2 scheduale tasks.
first one "import new feeds" and this run every day to get new feeds and store it.
second one "update top five feeds" which calculate rate of articles and give them degree per rate
and it will running every 5 mins as required.

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
