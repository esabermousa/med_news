from flask import Blueprint, request
from flask import current_app as app

from app.util import create_response, serialize_list
from app.auth import auth
from app.data_sources import Reddit


news = Blueprint("news", __name__)


@news.route("/", methods=["GET"])
@auth.login_required
def list_news():
    all_news = list()
    reddit = Reddit()
    reddit_news = reddit.list_news()
    all_news += serialize_list(reddit_news, 'reddit', app.config.get('TEDDIT'))
    return create_response(message='ok', data={'result': all_news})


