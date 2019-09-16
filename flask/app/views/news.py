from flask import Blueprint, request
from flask import current_app as app

from app.util import create_response, serialize_list
from app.auth import auth
from app.data_sources import Reddit, Newsapi


news = Blueprint("news", __name__)


@news.route("/", methods=["GET"])
@auth.login_required
def list_news():
    query = request.args.get('query')
    all_news = list()
    reddit = Reddit()
    news_api = Newsapi()
    
    # search for news
    if query:
        reddit_news = reddit.search_news(str(query))
        all_news += serialize_list(reddit_news, 'reddit', app.config.get('REDDIT'))
        
        news_api_news = news_api.search_news(str(query))
        all_news += serialize_list(news_api_news, 'newsapi', app.config.get('NEWSAPI'))
        
        msg = "Successfully Search For {} in news.".format(str(query))
        app.logger.info(msg)
        return create_response(message=msg, data={'news': all_news})


    # List All news    
    reddit_news = reddit.list_news()
    all_news += serialize_list(reddit_news, 'reddit', app.config.get('REDDIT'))
    
    news_api_news = news_api.list_news()
    all_news += serialize_list(news_api_news, 'newsapi', app.config.get('NEWSAPI'))
    
    msg = "Successfully list news."
    app.logger.info(msg)
    return create_response(message=msg, data={'news': all_news})


