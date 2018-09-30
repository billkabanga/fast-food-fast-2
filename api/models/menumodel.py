"""
module menumodel
"""
import re
from flask import current_app as app, make_response, jsonify
from dbcontroller import Dbcontroller

class Menu:
    """
    class for menu
    """
    def __init__(self, item, price):
        """
        constructor method for menu class
        :param item:
        :param price:
        """
        self.item = item
        self.price = price
    def add_food(self):
        """
        method adds new food option to menu
        """
        query = "INSERT INTO menu(item, price) VALUES('{}','{}')\
         RETURNING menuid".format(self.item, self.price)
        new_db = Dbcontroller(app.config['DATABASE_URL'])
        return new_db.post_data(query)
    @classmethod
    def get_menu(cls):
        """
        method for fetching menu items from database
        """
        query = "SELECT * FROM menu"
        new_db = Dbcontroller(app.config['DATABASE_URL'])
        menu = new_db.get_all_data(query)
        response = []
        for item in menu:
            orders = {}
            orders['menuid'] = item[0]
            orders['item'] = item[1]
            orders['price'] = item[2]
            response.append(orders)
        return response
    @staticmethod
    def validate_food_input(item):
        """
        method validates food input
        :param item:
        """
        if item.strip() == '':
            return make_response(jsonify({'message': 'Food item cannot be empty'}), 400)
        if not re.match(r"^[a-zA-Z ]+$", item):
            return make_response(jsonify({'message': 'Food item should only have letters'}), 400)
        return True
