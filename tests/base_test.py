"""
module base_test
"""
import unittest
from flask import current_app as app
from api import create_app
from api.models.dbcontroller import Dbcontroller
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
        
    def tearDown(self):
        """
        method clears tests database after tests
        """
        new_db = Dbcontroller(app.config['DATABASE_URL'])
        new_db.drop_tables()
