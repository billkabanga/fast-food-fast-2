"""
module orderview
"""
from flasgger import swag_from
from flask import Blueprint, jsonify, make_response
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import (jwt_required, get_jwt_identity)
from api.models.usermodel import Users
from api.models.ordermodel import Orders

order_blue_print = Blueprint('order_bp', __name__, url_prefix='/api/v1')
api = Api(order_blue_print)


class OrderHandler(Resource):
    """
    class handles orders requests
    """

    def __init__(self):
        """
        constructor method for order handler class
        """
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'item', type=str, required=True, help='no food item to add')
        self.reqparse.add_argument(
            'quantity',
            type=int,
            required=True,
            help='Please provide quantity')

    @jwt_required
    @swag_from('../docs/place_order.yml', methods=['POST'])
    def post(self):
        """
        post request method for new order
        """
        args = self.reqparse.parse_args()
        logged_in = get_jwt_identity()
        admin = Users.get_admin(logged_in)
        valid_data = Orders.validate_order(args['item'])
        if logged_in and not admin:
            if valid_data == True:
                price = Orders.get_price(args['quantity'], args['item'])
                contact = Orders.get_user_contact(logged_in)
                response = Orders(args['item'], args['quantity'], price,
                                  logged_in, contact)
                result = response.add_order()
                if result:
                    return make_response(
                        jsonify({
                            'message': 'Order placed successfully'
                        }), 201)
            return valid_data
        return make_response(
            jsonify({
                'message': 'Transaction available to only client user'
            }), 403)

    @jwt_required
    @swag_from('../docs/get_history.yml', methods=['GET'])
    def get(self):
        """
        get request method for order history
        """
        logged_in = get_jwt_identity()
        admin = Users.get_admin(logged_in)
        if logged_in and not admin:
            result = Orders.get_order_history(logged_in)
            if result:
                return result
            return make_response(jsonify({'message': 'No orders found'}), 404)
        return make_response(
            jsonify({
                'message': 'Transaction available to only client user'
            }), 403)


class OrdersGetter(Resource):
    """
    class for getting all orders
    """

    @jwt_required
    @swag_from('../docs/get_orders.yml', methods=['GET'])
    def get(self):
        """
        get request method for all orders
        """
        logged_in = get_jwt_identity()
        admin = Users.get_admin(logged_in)
        if logged_in and admin:
            result = Orders.get_orders()
            if result:
                return result
            return make_response(jsonify({'message': 'No orders found'}), 404)
        return make_response(
            jsonify({
                'message': 'Transaction available to only admin user'
            }), 403)


class SpecificOrder(Resource):
    """
    class handles request methods for specific order
    """

    def __init__(self):
        """
        constructor method for order handler class
        """
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'order_status',
            type=str,
            required=True,
            help='please provide order status')

    @jwt_required
    @swag_from('../docs/get_order.yml', methods=['GET'])
    def get(self, orderId):
        """
        method for get request for specific order
        """
        logged_in = get_jwt_identity()
        admin = Users.get_admin(logged_in)
        if logged_in and admin:
            result = Orders.get_specific_order(orderId)
            if result:
                return result
            return make_response(jsonify({'message': 'Order not found'}), 404)
        return make_response(
            jsonify({
                'message': 'Transaction available to only admin user'
            }), 403)

    @jwt_required
    @swag_from('../docs/update_status.yml', methods=['PUT'])
    def put(self, orderId):
        """
        method for put request to update order_status
        """
        args = self.reqparse.parse_args()
        logged_in = get_jwt_identity()
        admin = Users.get_admin(logged_in)
        if logged_in and admin:
            result = Orders.update_status(orderId, args['order_status'])
            if result == True:
                return make_response(
                    jsonify({
                        'message': 'Order status updated'
                    }), 201)
            return result
        return make_response(
            jsonify({
                'message': 'Transaction available to only admin user'
            }), 403)


api.add_resource(OrderHandler, '/users/orders')
api.add_resource(OrdersGetter, '/orders')
api.add_resource(SpecificOrder, '/orders/<int:orderId>')
