"""
module init
"""
from flask import Flask
from config import DevelopmentConfig
from api.views.userview import user_blue_print

def create_app():
    """
    function creates app
    """
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    app.register_blueprint(user_blue_print)
    return app
