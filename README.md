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
7. [Usage](#usage)

### Problem
>We need to integrate multiple news resources in one service and deal with all with same protocol.

### Solution
> I used 3rd party APIs for each news resources like [newsapi-python](https://github.com/mattlisiv/newsapi-python) for News API , [PRAW](https://github.com/praw-dev/praw/) for Reddit and produce just one endpoint that interact all of them.

> First you have to login `/login` to get token to use other endpoints.

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
### Usage
1. Login endpoint `/login` GET
**Request URL:** http://<span></span>your_domain/login <br/>
**Description:** This endpoint will allow user to communicate with other endpoints securely.

#### Request Parameters

Name | Type | Description | Required | Permitted Parameter Type
---- | ---- | ----------- | -------- | ------------------------
auth | String | Username and password. **Format:** username:password | Yes | Body

#### Response Parameters

Name | Type | Description
-----| -----| ----
result | Object | Object That have (auth_token, expiration, return_message)
success | Boolean | Validity of request
auth_token | String | Token used to make requests
expiration | Int | Validity of auth_token in minutes
return_message | String | Message specifying operation information

#### Status Codes

HTTP Status Code | Return Message
---|----
200 | “Success”
400 | “Mandatory fields are not supplied”
401 | “Invalid authentication credentials”
500 | “Failed to login user”


#### Sample Request
```
POST /login HTTP/1.1
Accept: application/json

{
   "auth":"username:password",
}
```

#### Sample Response
```
{
    "result": {
        "auth_token": "eyJhbGciOiJIUzUxMiIsImlhdCI6MTU2ODY5ODY.....",
        "expiration": 60,
        "return_message": "Successfully loged in."
    },
    "success": true
}
```
-------------------------------------------------------------------------------------------

2. List News `/news` GET
**Request URL:** http://<span></span>your_domain/news <br/>
**Description:** This endpoint List all news from news api and reddit.

#### Request Header

Name | Type | Description | Required | Permitted Parameter Type
---- | ---- | ----------- | -------- | ------------------------
Authorization | Token | 'Bearer ' + token(string) | Yes | Body



#### Response Parameters

Name | Type | Description
-----| -----| ----
result | Object | Object That have (auth_token, expiration, return_message)
success | Boolean | Validity of request
headline | String | Title of news
link | String | Link for news
source | String | source for news

#### Sample Response
```
{
    "result": [
					  {
						"headline": "Human organs can be stored for three times as long in major breakthrough for transplants", 
						"link": "https://www.telegraph.co.uk/science/2019/09/09/human-organs-can-stored-three-times-long-major-breakthrough/",
						"source": "reddit" 
					  },
					  {
						"headline": "Depth of Field: The Shared Memory of One World Trade Center",
						"link": "https://www.wired.com/story/one-world-trade-center-history-future/",
						"source": "newsapi"
					  },
					],
    "success": true
}
```
-------------------------------------------------------------------------------------------

3. Search News `/news?query=bitcoin` GET
**Request URL:** http://<span></span>your_domain/news?query=bitcoin <br/>
**Description:** This endpoint search for news that have bitcoin term from news api and reddit.

#### Request Header

Name | Type | Description | Required | Permitted Parameter Type
---- | ---- | ----------- | -------- | ------------------------
Authorization | Token | 'Bearer ' + token(string) | Yes | Body

#### Request Parameters

Name | Type | Description | Required | Permitted Parameter Type
---- | ---- | ----------- | -------- | ------------------------
query | String | Term that you need to search for | Yes | Body

#### Response Parameters

Name | Type | Description
-----| -----| ----
result | Object | Object That have (auth_token, expiration, return_message)
success | Boolean | Validity of request
headline | String | Title of news
link | String | Link for news
source | String | source for news

#### Sample Response
```
{
    "result": [
					  {
						"headline": "Human organs can be stored for three times as long in major breakthrough for transplants", 
						"link": "https://www.telegraph.co.uk/science/2019/09/09/human-organs-can-stored-three-times-long-major-breakthrough/",
						"source": "reddit" 
					  },
					  {
						"headline": "Depth of Field: The Shared Memory of One World Trade Center",
						"link": "https://www.wired.com/story/one-world-trade-center-history-future/",
						"source": "newsapi"
					  },
					],
    "success": true
}
```