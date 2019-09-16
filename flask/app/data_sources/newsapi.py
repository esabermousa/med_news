from newsapi import NewsApiClient
from flask import current_app as app


class Newsapi():
    def __init__(self):
        self.api = NewsApiClient(api_key=app.config.get('NEWSAPI_KEY'))

    def list_news(self):
        all_news = self.api.get_everything()
        app.logger.info("List top news from newsapi.")
        if 'status' in all_news.keys() and all_news.get('status') == 'ok':        
            return all_news['articles']
        
        return list()

    def search_news(self, query):
        result_news = self.api.get_everything(q=query)
        app.logger.info("Search for {}  from apinews news.".format(str(query)))
        if 'status' in result_news.keys() and result_news.get('status') == 'ok':        
            return result_news['articles']
        
        return list()
