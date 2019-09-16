import json
from app.models import db

def test_health(client):
    rs = client.post("/health-check")
    assert rs.status_code == 200

def test_registeration(client):
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "username": "test",
        "password": "pass"
    }
    rs = client.post("/registration", data=json.dumps(data), headers=headers)
    assert rs.status_code == 200
    ret_dict = rs.json
    assert ret_dict["success"] == True


def test_login(client):
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "username": "test",
        "password": "pass"
    }

    rs = client.post("/login", data=json.dumps(data), headers=headers)
    assert rs.status_code == 200
    ret_dict = rs.json
    assert ret_dict["success"] == True
    return ret_dict


def test_logout(client):
    login_result = test_login(client)
    access_token = login_result["result"]["access_token"]

    headers = {
        "Content-Type": "application/json",
        "Authorization": 'Bearer ' + access_token
    }
    rs = client.post("/logout", headers=headers)
    assert rs.status_code == 200
    ret_dict = rs.json
    assert ret_dict["success"] == True


def test_logout_refresh(client):
    login_result = test_login(client)
    refresh_token = login_result["result"]["refresh_token"]

    headers = {
        "Content-Type": "application/json",
        "Authorization": 'Bearer ' + refresh_token
    }
    rs = client.post("/logout_refresh", headers=headers)
    assert rs.status_code == 200
    ret_dict = rs.json
    assert ret_dict["success"] == True


def test_refresh_token(client):
    login_result = test_login(client)
    refresh_token = login_result["result"]["refresh_token"]

    headers = {
        "Content-Type": "application/json",
        "Authorization": 'Bearer ' + refresh_token
    }
    rs = client.post("/refresh_token", headers=headers)
    assert rs.status_code == 200
    ret_dict = rs.json
    assert ret_dict["success"] == True

