from app.core import create_response, logger
from flask import Blueprint, request

# from app.auth import verify_user


main = Blueprint("main", __name__)


@main.route("/health-check", methods=["GET"])
def index():
    msg = "Health-check success."
    logger.info(msg)
    return create_response(message=msg, data={})


@main.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    logger.info("Data recieved: %s", data)

    if "auth" not in data:
        msg = "No auth provided."
        logger.info(msg)
        return create_response(status=400, message=msg)
    
    if ":" not in data['auth']:
        msg = "Username or Password is missing."
        logger.info(msg)
        return create_response(status=400, message=msg, data={})    

    username = data['auth'].split(':')[0]
    password = data['auth'].split(':')[-1]
    # token = verify_user(data['username'], data['password'])
    token = 'asddfffgfgfhfjhhjgjkgujnvbnbn'
    if token:
        result = {
            "auth_token": token,
            "expiration": 60
        }
        msg = "Successfully loged in."
        logger.info(msg)
        return create_response(message=msg, data=result)