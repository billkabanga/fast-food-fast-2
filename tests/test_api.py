"""
module test_api
"""
from tests.base_test import BaseTest

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
        with self.client as client:
            response = client.post(BASE_URL+'/auth/signup', json=dict(self.user))
            self.assertEqual(response.status_code, 201)
    def test_empty_username(self):
        """
        test method for empty username on signup
        asserts status code is 400
        """
        with self.client as client:
            response = client.post(BASE_URL+'/auth/signup', json=dict(self.empty_name))
            self.assertEqual(response.status_code, 400)
    def test_invalid_role(self):
        """
        test method for invalid role on signup
        asserts status code is 400
        """
        with self.client as client:
            response = client.post(BASE_URL+'/auth/signup', json=dict(self.invalid_role))
            self.assertEqual(response.status_code, 400)
    def test_user_login(self):
        """
        test method for user login
        asserts status code is 200
        """
        with self.client as client:
            client.post(BASE_URL+'/auth/signup', json=dict(self.user))
            response = client.post(BASE_URL+'/auth/login', json=dict(self.login))
            self.assertEqual(response.status_code, 200)
