import os
import logging

from flask import Flask, request
from dotenv import load_dotenv

from app.config import config
from app.util import all_exception_handler

    
def create_app():
    app = Flask(__name__)
    env = os.environ.get("FLASK_ENV", "development")
    app.config.from_object(config[env])
    
    # load dotenv in the base root
    APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    dotenv_path = os.path.join(APP_ROOT, '.env')
    load_dotenv(dotenv_path)

    # logging
    setup_logging(app)

    # import and register blueprints
    from app.views import main
    from app.views import news

    app.register_blueprint(main.main)
    app.register_blueprint(news.news, url_prefix='/news')

    # register error Handler
    app.register_error_handler(Exception, all_exception_handler)

    return app


class RequestFormatter(logging.Formatter):
    def format(self, record):
        record.url = request.url
        record.remote_addr = request.remote_addr
        return super().format(record)


def setup_logging(app):
    formatter = RequestFormatter(
    "%(asctime)s %(remote_addr)s: requested %(url)s: %(levelname)s in [%(module)s: %(lineno)d]: %(message)s")
    if app.config.get("LOG_FILE"):
        fh = logging.FileHandler(app.config.get("LOG_FILE"))
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        app.logger.addHandler(fh)
