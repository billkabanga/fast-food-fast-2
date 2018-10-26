"""
module ordermodel
"""
import json
import datetime
from flask import jsonify, make_response, current_app as app
from api.models.dbcontroller import Dbcontroller


def datetime_converter(order_date):
    """
    function converts date to string
    """
    if isinstance(order_date, datetime.datetime):
        return order_date.__str__()
    raise TypeError("Unknown type not Json serializable")


class Orders:
    """
    class for orders data
    """

    def __init__(self, item, quantity, price, client, contact):

        self.item = item
        self.quantity = quantity
        self.price = price
        self.order_date = datetime.datetime.now().strftime(
            "%A, %d %B %Y %I:%M%p")
        self.order_status = 'New'
        self.client = client
        self.contact = contact

    def add_order(self):
        """
        method adds new order to orders
        """
        query = "INSERT INTO orders(item, quantity, price, order_date, order_status, client, contact)\
        VALUES('{}','{}','{}','{}','{}','{}','{}')".format(
            self.item, self.quantity, self.price, self.order_date,
            self.order_status, self.client, self.contact)
        new_db = Dbcontroller(app.config['DATABASE_URL'])
        return new_db.post_data(query)

    @classmethod
    def get_orders(cls):
        """
        method for fetching orders from database
        """
        query = "SELECT * FROM orders"
        new_db = Dbcontroller(app.config['DATABASE_URL'])
        orders = new_db.get_all_data(query)
        response = []
        for order in orders:
            odrs = {}
            odrs['orderid'] = order[0]
            odrs['item'] = order[1]
            odrs['quantity'] = order[2]
            odrs['price'] = order[3]
            odrs['order_date'] = json.dumps(
                order[4], default=datetime_converter)
            odrs['order_status'] = order[5]
            odrs['client'] = order[6]
            odrs['contact'] = order[7]
            response.append(odrs)
        return response

    @classmethod
    def get_specific_order(cls, orderId):
        """
        method for fetching orders from database
        """
        query = "SELECT * FROM orders where orderid = '{}'".format(orderId)
        new_db = Dbcontroller(app.config['DATABASE_URL'])
        order = new_db.get_data(query)
        if order:
            odr = {}
            odr['orderid'] = order[0]
            odr['item'] = order[1]
            odr['quantity'] = order[2]
            odr['price'] = order[3]
            odr['order_date'] = json.dumps(
                order[4], default=datetime_converter)
            odr['order_status'] = order[5]
            odr['client'] = order[6]
            odr['contact'] = order[7]
            if order[0] == orderId:
                return jsonify({'odr': odr})
        return make_response(jsonify({'message': 'Order not found'}), 404)

    @staticmethod
    def validate_order(order_item):
        """
        method validates order inputs
        :param order_item:
        """
        query = "SELECT * FROM menu WHERE item = '{}'".format(order_item)
        new_db = Dbcontroller(app.config['DATABASE_URL'])
        menu = new_db.get_all_data(query)
        for item in menu:
            orders = {}
            orders['menuid'] = item[0]
            orders['item'] = item[1]
            orders['price'] = item[2]
            if orders['item'] == order_item:
                return True
            return make_response(
                jsonify({
                    'message': 'Food item not available, check menu'
                }), 404)
        return make_response(
            jsonify({
                'message': 'Food item not available, check menu'
            }), 404)

    @classmethod
    def get_price(cls, quantity, order_item):
        """
        method gets price for the placed order
        """
        query = "SELECT * FROM menu WHERE item = '{}'".format(order_item)
        new_db = Dbcontroller(app.config['DATABASE_URL'])
        menu = new_db.get_all_data(query)
        for item in menu:
            orders = {}
            orders['menuid'] = item[0]
            orders['item'] = item[1]
            orders['price'] = item[2]
            if quantity > 0:
                cls.price = orders['price'] * quantity
                return cls.price
            return make_response(
                jsonify({
                    'message': 'Quantity must be greater than 0'
                }), 400)
    
    @classmethod
    def check_existing_order(cls, orderId):
        query = "SELECT orderid FROM orders where orderid = '{}'".format(orderId)
        new_db = Dbcontroller(app.config['DATABASE_URL'])
        order = new_db.get_data(query)
        return order

    @classmethod
    def update_status(cls, orderId, order_status):
        """
        class method updates order_status
        """
        order_stat = ("Processing", "Cancelled", 'Complete')
        if order_status in order_stat:
            order = cls.check_existing_order(orderId)
            if order:
                query = "UPDATE orders SET order_status = '{}' WHERE orderid = '{}'".format(
                    order_status, orderId)
                new_db = Dbcontroller(app.config['DATABASE_URL'])
                return new_db.post_data(query)
            return make_response(
                jsonify({
                    'message':
                    'Order of choice not found'
                }), 404)

        return make_response(
            jsonify({
                'message':
                'Status can only be Processing, Cancelled, Complete'
            }), 400)

    @classmethod
    def get_order_history(cls, username):
        """
        method for fetching order history from database
        """
        query = "SELECT * FROM orders WHERE client = '{}'".format(username)
        new_db = Dbcontroller(app.config['DATABASE_URL'])
        orders = new_db.get_all_data(query)
        response = []
        for order in orders:
            odrs = {}
            odrs['orderid'] = order[0]
            odrs['item'] = order[1]
            odrs['quantity'] = order[2]
            odrs['price'] = order[3]
            odrs['order_date'] = json.dumps(
                order[4], default=datetime_converter)
            odrs['order_status'] = order[5]
            response.append(odrs)
        return response

    @classmethod
    def get_user_contact(cls, username):
        """
        method gets client's contact
        """
        query = "SELECT * FROM users where username = '{}'".format(username)
        new_db = Dbcontroller(app.config['DATABASE_URL'])
        user = new_db.get_all_data(query)
        for con in user:
            return con[3]
