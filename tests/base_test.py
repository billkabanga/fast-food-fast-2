"""
module base_test
"""
import unittest
from flask import current_app as app
from api import create_app
from dbcontroller import Dbcontroller
from config import TestingConfig

class BaseTest(unittest.TestCase):
    """
    class for the base test
    """
    def new_test_app(self):
        """
        method creates app for the tests
        """
        app = create_app()
        app.config.from_object(TestingConfig)
        return app

    def setUp(self):
        """
        method sets up new application, testclient for the tests
        creates an instance of the database for the tests
        """
        self.app = self.new_test_app()
        self.client = self.app.test_client()
        self.app.app_context().push()
        new_db = Dbcontroller(app.config['DATABASE_URL'])
        new_db.create_tables()
        self.user = {
            "username": "kabangabill",
            "email": "tkbillkabanga@gmail.com",
            "contact": "0784318356",
            "password": "0123456789",
            "role": "admin"
        }
        self.client_user = {
            "username": "james",
            "email": "james@gmail.com",
            "contact": "0784318356",
            "password": "0123456789",
            "role": "client"
        }
        self.empty_name = {
            "username": "       ",
            "email": "tkbillkabanga@gmail.com",
            "contact": "0784318356",
            "password": "0123456789",
            "role": "admin"
        }
        self.invalid_role = {
            "username": "kabangabill",
            "email": "tkbillkabanga@gmail.com",
            "contact": "0784318356",
            "password": "0123456789",
            "role": "whoisthis"
        }
        self.login = {
            "username": "kabangabill",
            "password": "0123456789"
        }
        self.login_client = {
            "username": "james",
            "password": "0123456789"
        }
        self.order = {
            "item": "chicken",
            "price": "15000"
        }
        self.empty_item = {
            "item": "     ",
            "price": "15000"
        }
        self.invalid_item = {
            "item": "89798**-",
            "price": "5000"
        }
    def tearDown(self):
        """
        method clears tests database after tests
        """
        new_db = Dbcontroller(app.config['DATABASE_URL'])
        new_db.drop_tables()
