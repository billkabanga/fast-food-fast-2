"""
module menuview
"""
from flask import Blueprint, jsonify, make_response, current_app as app
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import (jwt_required, get_jwt_identity)
from api.models.dbcontroller import Dbcontroller
from api.models.usermodel import Users
from api.models.menumodel import Menu

mn_blue_print = Blueprint('menu_bp', __name__, url_prefix='/api/v1')
api = Api(mn_blue_print)


class MenuHandler(Resource):
    """
    class handles menu requests
    """

    def __init__(self):
        """
        constructor method for menu handler class
        """
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'item', type=str, required=True, help='no food item to add')
        self.reqparse.add_argument(
            'price', type=int, required=True, help='Please provide price')

    @jwt_required
    def post(self):
        """
        post request method for new food item
        """
        args = self.reqparse.parse_args()
        logged_in = get_jwt_identity()
        admin = Users.get_admin(logged_in)
        valid_data = Menu.validate_food_input(args['item'])
        if logged_in and admin:
            if valid_data == True:
                response = Menu(args['item'], args['price'])
                query = "SELECT * FROM menu WHERE item = '{}'".format(
                    args['item'])
                new_db = Dbcontroller(app.config['DATABASE_URL'])
                exist = new_db.get_data(query)
                if exist:
                    return make_response(
                        jsonify({
                            'message': 'Food option already exists'
                        }), 400)
                result = response.add_food()
                if result:
                    return make_response(
                        jsonify({
                            'message': 'Food option added successfuly'
                        }), 201)
            return valid_data
        return make_response(
            jsonify({
                'message': 'Transaction available to only admin user'
            }), 400)

    def get(self):
        """
        get method for available menu
        """
        result = Menu.get_menu()
        if result:
            return result
        return make_response(
            jsonify({
                'message': 'No available food items'
            }), 404)


api.add_resource(MenuHandler, '/menu')
