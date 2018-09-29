"""
module init
"""
from flask import Flask
from config import DevelopmentConfig

def create_app():
    """
    function creates app
    """
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    return app
    