import json
import pytest

from app import create_app
from app.config import TestingConfig
from app.auth import generate_auth_token


@pytest.fixture(scope="session")
def client():
    app = create_app("test")
    app.app_context().push()

    client = app.test_client()
    yield client

def test_health(client):
    rs = client.get("/health-check")
    assert rs.status_code == 200


def test_login(client):
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "auth": "eslam:password"
    }

    rs = client.post("/login", data=json.dumps(data), headers=headers)
    assert rs.status_code == 200
    ret_dict = rs.json
    assert ret_dict["success"] == True
    return ret_dict


def test_missing_login_fields(client):
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "auth": "eslam"
    }

    rs = client.post("/login", data=json.dumps(data), headers=headers)
    assert rs.status_code == 400
    ret_dict = rs.json
    assert ret_dict["success"] == False
    return ret_dict


def test_wrong_login(client):
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "auth": "eslam:wrongpassword"
    }

    rs = client.post("/login", data=json.dumps(data), headers=headers)
    assert rs.status_code == 401
    ret_dict = rs.json
    assert ret_dict["success"] == False
    return ret_dict


def test_list_news(client):
    token = generate_auth_token("eslam")
    
    headers = {
        'Authorization': 'Bearer ' + token
    }
    rs = client.get("/news", headers=headers, follow_redirects=True)
    # assert rs.status_code == 200
    # ret_dict = rs.json
    # assert ret_dict["location"] == True
    # return ret_dict


# def test_search_news(client):
#     token = generate_auth_token("eslam")
    
#     headers = {
#         'Authorization': 'Bearer ' + token
#     }
#     rs = client.get("/news", headers=headers, follow_redirects=True)

#     # assert rs.status_code == 200
#     # ret_dict = rs.json
#     # assert ret_dict["location"] == True
#     # return ret_dict