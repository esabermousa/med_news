import praw
from flask import current_app as app


class Reddit():

    def __init__(self):
        self.reddit = praw.Reddit(client_id=app.config.get('REDDIT_CLIENT_ID'), 
                                  client_secret=app.config.get('REDDIT_CLIENT_SECRET'),
                                  password=app.config.get('REDDIT_PASSWORD'),
                                  user_agent=app.config.get('REDDIT_USERAGENT'),
                                  username=app.config.get('REDDIT_USERNAME'))

    def list_news(self):
        top_news = self.reddit.subreddit('news').new()
        return top_news

    def search_news(self, query):
        result_news = self.reddit.subreddit('news').search(str(query))
        return result_news
