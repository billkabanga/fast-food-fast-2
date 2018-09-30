"""
module test_menu
"""
import json
from tests.base_test import BaseTest

BASE_URL = '/api/v1'

class MenuTest(BaseTest):
    """
    class for tests for menu endpoints
    """
    def test_add_food(self):
        """
        test method for adding food item
        asserts response status is 201
        """
        with self.client as client:
            client.post(BASE_URL+'/auth/signup',json=dict(self.user))
            response = client.post(BASE_URL+'/auth/login',json=dict(self.login))
            response_data = json.loads(response.data.decode())
            test_response = client.post(BASE_URL+'/menu', headers={'Authorization': 'Bearer '+ response_data['access_token']},\
            json=dict(self.order))
            self.assertEqual(test_response.status_code, 201)
    def test_client_user_not_allowed(self):
        """
        test method for adding food item
        asserts response status is 400
        """
        with self.client as client:
            client.post(BASE_URL+'/auth/signup',json=dict(self.client_user))
            response = client.post(BASE_URL+'/auth/login',json=dict(self.login_client))
            response_data = json.loads(response.data.decode())
            test_response = client.post(BASE_URL+'/menu', headers={'Authorization': 'Bearer '+ response_data['access_token']},\
            json=dict(self.order))
            self.assertEqual(test_response.status_code, 400)
    def test_empty_food_item(self):
        """
        test method for empty food item
        asserts response status is 400
        """
        with self.client as client:
            client.post(BASE_URL+'/auth/signup',json=dict(self.user))
            response = client.post(BASE_URL+'/auth/login',json=dict(self.login))
            response_data = json.loads(response.data.decode())
            test_response = client.post(BASE_URL+'/menu', headers={'Authorization': 'Bearer '+ response_data['access_token']},\
            json=dict(self.empty_item))
            self.assertEqual(test_response.status_code, 400)
    def test_ivalid_food(self):
        """
        test method for invalid food input
        asserts response status is 400
        """
        with self.client as client:
            client.post(BASE_URL+'/auth/signup',json=dict(self.user))
            response = client.post(BASE_URL+'/auth/login',json=dict(self.login))
            response_data = json.loads(response.data.decode())
            test_response = client.post(BASE_URL+'/menu', headers={'Authorization': 'Bearer '+ response_data['access_token']},\
            json=dict(self.invalid_item))
            self.assertEqual(test_response.status_code, 400)
    