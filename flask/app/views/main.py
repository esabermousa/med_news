from app.util import create_response
from flask import Blueprint, request, g
from flask import current_app as app

from app.auth import auth, generate_auth_token


main = Blueprint("main", __name__)


@main.route("/health-check", methods=["GET"])
def index():
    msg = "Health-check success."
    app.logger.info(msg)
    return create_response(message=msg, data={})


@main.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    app.logger.info("Data recieved: %s", data)

    if "auth" not in data:
        msg = "No auth provided."
        app.logger.info(msg)
        return create_response(status=400, message=msg, data={})
    
    if ":" not in data['auth']:
        msg = "Username or Password is missing."
        app.logger.info(msg)
        return create_response(status=400, message=msg, data={})    

    username = str(data['auth'].split(':')[0])
    password = str(data['auth'].split(':')[-1])

    if username == app.config.get('AUTH_USERNAME') and password == app.config.get('AUTH_PASSWORD'):
        token = generate_auth_token(username)
        result = {
            "auth_token": token,
            "expiration": 60
        }
        msg = "Successfully loged in."
        app.logger.info(msg)
        return create_response(message=msg, data=result)

    msg = "Username or Password is wrong."
    app.logger.info(msg)
    return create_response(status=401, message=msg, data={})