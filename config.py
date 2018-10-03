"""
module config
"""
class Config:
    """
    parent config class
    """
    DEBUG = False

class DevelopmentConfig(Config):
    """
    class for development configuration
    """
    DEBUG = True
    DATABASE_URL = 'postgres://postgres:focus2red@localhost:5432/fastfoodfastdb'
class TestingConfig(Config):
    """
    class for testing configuration
    """
    DEBUG = True
    TESTING = True
    DATABASE_URL = 'postgres://postgres:focus2red@localhost:5432/fastfoodtestdb'
