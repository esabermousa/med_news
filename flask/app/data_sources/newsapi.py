import praw


class Newsapi():

    def __init__(self):
        self.reddit = praw.Reddit(client_id='CLIENT_ID', client_secret="CLIENT_SECRET",
                             password='PASSWORD', user_agent='USERAGENT',
                             username='USERNAME')

    def list_news(self):
        news = self.reddit.subreddit('news').top()
        print(news)

    def search_news(self):
        pass
