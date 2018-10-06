"""
module init
"""
from flask import Flask, make_response, jsonify
from flask_jwt_extended import JWTManager
from config import DevelopmentConfig
from api.views.userview import user_blue_print
from api.views.menuview import mn_blue_print
from api.views.orderview import order_blue_print
from flasgger import Swagger


def wrong_url(error):
    """
    function for custom error handling
    """
    return make_response(jsonify({'message': 'Wrong URL entry'}), 404)


def create_app():
    """
    function creates app
    registers blueprint
    initialises JWTManager with flask app
    sets secret key
    """
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'SECRET'
    app.register_blueprint(user_blue_print)
    app.register_blueprint(mn_blue_print)
    app.register_blueprint(order_blue_print)
    app.register_error_handler(404, wrong_url)
    JWTManager(app)
    Swagger(app)
    return app
