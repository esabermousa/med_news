# med_news Aggregator

>It aggregates news from two different APIs [Reddit](https://www.reddit.com/dev/api/ "Reddit") and [News API](https://newsapi.org/ "News API").
It produces result in JSON format. There are two functionalities "list" and "search".

## Table of Contents
1. [Problem](#problem)
2. [Solution](#solution)
3. [Technologies](#technologies)
4. [Install](#install)
5. [Testing](#testing)
6. [Deploy](#deploy)

### Problem
>We need to integrate multiple news resources in one service and deal with all with same protocol.

### Solution
> I used 3rd party APIs for each news resources like [newsapi-python](https://github.com/mattlisiv/newsapi-python) for News API , [PRAW](https://github.com/praw-dev/praw/) for Reddit and produce just one endpoint that interact all of them.

>There are 2 endpoint List  `/news` to list all news, Search `/news?query=bitcoin` to search for specific term in news.

### Technologies
- python 3.6
- Flask Web Framework
- newsapi-python
- praw
- nginx
- Docker
- Docker-compose
- Pytest

### Install
1. clone repo.
```
$ git clone https://github.com/esabermousa/med_news 
```

2. move to repo. 
```
$ cd med_news
```

3. create virtualenv. 
NOTE: prerquiest to install `virtualenv`
```
$ virtualenv env -p python3.6
```

4. install requirements
```
$ source env/bin/activate
$ pip install -r flask/requirements.txt
```

5. add config variables
```
$ cp .env.example .env
```

6. add required field "3rd party api keys"
7. run app.
```
$ python flask/manage.py runserver
```


### Testing
```
$ cd flask/
$ pytest
```
### Deploy

1. install Docker and Docker-compose
You have to have installed [docker](https://www.docker.com/) & [docker-compose](https://docs.docker.com/compose/install/) in other to make it work.

2. build and run containers
```
$ docker-compose up -d
```
3. SSH into the container
```
$ docker-compose exec flask /bin/bash
```

4. Run unit test
```
$ pytets
```
