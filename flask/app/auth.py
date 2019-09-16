from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from flask import current_app as app
from flask import g

auth = HTTPTokenAuth('Bearer')


def generate_auth_token(username, password, expiration= 3600):
    s = Serializer(app.config.get('SECRET_KEY'), expires_in=expiration)
    return s.dumps({'username': username}).decode('utf-8')


@auth.verify_token
def verify_token(token):
    g.user = None
    try:
        token_serializer = Serializer(
            app.config.get('SECRET_KEY'), expires_in=3600)
        data = token_serializer.loads(token)
    except:  # noqa: E722
        return False
    if 'username' in data:
        g.user = data['username']
        return True
    return False
