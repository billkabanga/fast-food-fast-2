"""
module base_test
"""
import unittest
import json
from flask import current_app as app
from api import create_app
from api.models.dbcontroller import Dbcontroller
from config import TestingConfig
from . import (USER, LOGIN, CLIENT_USER, LOGIN_CLIENT)
BASE_URL = '/api/v1'


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

    def login_admin(self):
        """
        method logs in admin user
        :return: access_token
        """
        self.client.post(BASE_URL + '/auth/signup', json=dict(USER))
        response = self.client.post(BASE_URL + '/auth/login', json=dict(LOGIN))
        response_data = json.loads(response.data.decode())
        return response_data['access_token']

    def login_client(self):
        """
        method logs in client user
        :return: access_token
        """
        self.client.post(BASE_URL + '/auth/signup', json=dict(CLIENT_USER))
        response = self.client.post(
            BASE_URL + '/auth/login', json=dict(LOGIN_CLIENT))
        response_data = json.loads(response.data.decode())
        return response_data['access_token']

    def tearDown(self):
        """
        method clears tests database after tests
        """
        new_db = Dbcontroller(app.config['DATABASE_URL'])
        new_db.drop_tables()
