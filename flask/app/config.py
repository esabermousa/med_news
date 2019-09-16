import os

class Config:
    """
    Base Configuration
    """
    LOG_FILE = "app.log"  # where logs are outputted to
    SECRET_KEY = os.getenv("SECRET_KEY")
    AUTH_USERNAME = os.getenv("AUTH_USERNAME")
    AUTH_PASSWORD = os.getenv("AUTH_PASSWORD")

    # Reddit Creadintials
    REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")  # 2oRB4_NENWeSog
    REDDIT_CLIENT_SECRET = os.getenv(
        "REDDIT_CLIENT_SECRET")  # mmyBpGP-Vxi6TVcvtJtAXSob1GM
    REDDIT_PASSWORD = os.getenv("REDDIT_PASSWORD")
    REDDIT_USERAGENT = os.getenv("REDDIT_USERAGENT") 
    REDDIT_USERNAME = os.getenv("REDDIT_USERNAME")

    # Reddit Fields
    TEDDIT = [
        'header_title',
        'title',
        'url'
    ]
 
class DevelopmentConfig(Config):
    DEBUG = True


class DockerConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False



# way to map the value of `FLASK_ENV` to a configuration
config = {
    "development": DevelopmentConfig,
    "docker": DockerConfig,
    "production": ProductionConfig
    }
