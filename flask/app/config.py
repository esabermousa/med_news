import os

class Config:
    """
    Base Configuration
    """
    LOG_FILE = "app.log"  # where logs are outputted to
    BASIC_AUTH_FORCE = True
    SECRET_KEY = os.environ.get("SECRET_KEY")
    AUTH_USERNAME = os.environ.get("TAUH_USERNAME")
    AUTH_PASSWORD = os.environ.get("AUTH_PASSWORD")


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
