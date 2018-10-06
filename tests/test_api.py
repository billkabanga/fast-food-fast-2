"""
module test_api
"""
from tests.base_test import BaseTest

from . import (USER, EMPTY_NAME, INVALID_ROLE, LOGIN)

BASE_URL = '/api/v1'


class UserTest(BaseTest):
    """
    class for tests for user endpoints
    """

    def test_user_signup(self):
        """
        test method for user signup
        asserts status code is 201
        """
        response = self.client.post(BASE_URL + '/auth/signup', json=dict(USER))
        self.assertEqual(response.status_code, 201)

    def test_empty_username(self):
        """
        test method for empty username on signup
        asserts status code is 400
        """
        response = self.client.post(
            BASE_URL + '/auth/signup', json=dict(EMPTY_NAME))
        self.assertEqual(response.status_code, 400)

    def test_invalid_role(self):
        """
        test method for invalid role on signup
        asserts status code is 400
        """
        response = self.client.post(
            BASE_URL + '/auth/signup', json=dict(INVALID_ROLE))
        self.assertEqual(response.status_code, 400)

    def test_user_login(self):
        """
        test method for user login
        asserts status code is 200
        """
        self.client.post(BASE_URL + '/auth/signup', json=dict(USER))
        response = self.client.post(BASE_URL + '/auth/login', json=dict(LOGIN))
        self.assertEqual(response.status_code, 200)
