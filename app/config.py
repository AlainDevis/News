class Config:
    NEWS_SOURCE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey=6fae963c0fcf4d9aa800174be4f412fb'
    ARTICLES_URL = "https://newsapi.org/v2/everything?language=en&sources={}&apiKey=6fae963c0fcf4d9aa800174be4f412fb"


class ProdConfig(Config):
    pass

class DevConfig(Config):
    
    DEBUG = True