"""
module ordermodel
"""
import json
import datetime
from flask import current_app as app, jsonify, make_response
from dbcontroller import Dbcontroller

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
    def __init__(self, item, quantity, price, client):
        
        self.item = item
        self.quantity = quantity
        self.price = price
        self.order_date = datetime.datetime.now().strftime("%A, %d %B %Y %I:%M%p")
        self.order_status = 'New'
        self.client = client
    def add_order(self):
        """
        method adds new order to orders
        """
        query = "INSERT INTO orders(item, quantity, price, order_date, order_status, client)\
        VALUES('{}','{}','{}','{}','{}','{}')".format(
            self.item,
            self.quantity,
            self.price,
            self.order_date,
            self.order_status,
            self.client)
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
            odrs['order_date'] = json.dumps(order[4], default=datetime_converter)
            odrs['order_status'] = order[5]
            odrs['client'] = order[6]
            response.append(odrs)
        return response
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
            return make_response(jsonify({'message': 'Food item not available, check menu'}), 404)
        return make_response(jsonify({'message': 'Food item not available, check menu'}), 404)
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
            return make_response(jsonify({'message': 'Quantity must be greater than 0'}), 400)
