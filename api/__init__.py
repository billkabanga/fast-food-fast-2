"""
module init
"""
from flask import Flask
from flask_jwt_extended import JWTManager
from config import DevelopmentConfig
from api.views.userview import user_blue_print
from api.views.menuview import mn_blue_print

def create_app():
    """
    function creates app
    registers blueprint
    initialises JWTManager with flask app
    sets secret key
    """
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    app.config['JWT_SECRET_KEY'] = 'SECRET'
    app.register_blueprint(user_blue_print)
    app.register_blueprint(mn_blue_print)
    JWTManager(app)
    return app
