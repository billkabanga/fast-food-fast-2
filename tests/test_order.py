"""
module test_order
"""
import json
from tests.base_test import BaseTest

BASE_URL = '/api/v1'

class OrderTest(BaseTest):
    """
    class for tests for order endpoints
    """
    def test_place_order(self):
        """
        method tests place order endpoint
        asserts response status code is 201
        """
        with self.client as client:
            client.post(BASE_URL+'/auth/signup', json=dict(self.user))
            response = client.post(BASE_URL+'/auth/login', json=dict(self.login))
            response_data = json.loads(response.data.decode())
            client.post(
                BASE_URL+'/menu',
                headers={'Authorization': 'Bearer '+ response_data['access_token']},
                json=dict(self.order))
            client.post(BASE_URL+'/auth/signup', json=dict(self.client_user))
            response = client.post(BASE_URL+'/auth/login', json=dict(self.login_client))
            response_data = json.loads(response.data.decode())
            test_response = client.post(
                BASE_URL+'/users/orders',
                headers={'Authorization': 'Bearer '+ response_data['access_token']},
                json=dict(self.order_input))
            self.assertEqual(test_response.status_code, 201)
    def test_order_not_found(self):
        """
        method tests place order where order item is not on menu
        asserts response status code is 404
        """
        with self.client as client:
            client.post(BASE_URL+'/auth/signup', json=dict(self.user))
            response = client.post(BASE_URL+'/auth/login', json=dict(self.login))
            response_data = json.loads(response.data.decode())
            client.post(
                BASE_URL+'/menu',
                headers={'Authorization': 'Bearer '+ response_data['access_token']},
                json=dict(self.order))
            client.post(BASE_URL+'/auth/signup', json=dict(self.client_user))
            response = client.post(BASE_URL+'/auth/login', json=dict(self.login_client))
            response_data = json.loads(response.data.decode())
            test_response = client.post(
                BASE_URL+'/users/orders',
                headers={'Authorization': 'Bearer '+ response_data['access_token']},
                json=dict(self.new_item))
            self.assertEqual(test_response.status_code, 404)
    def test_admin_not_order(self):
        """
        method tests if admin wont place order
        asserts response status code is 400
        """
        with self.client as client:
            client.post(BASE_URL+'/auth/signup', json=dict(self.user))
            response = client.post(BASE_URL+'/auth/login', json=dict(self.login))
            response_data = json.loads(response.data.decode())
            client.post(
                BASE_URL+'/menu',
                headers={'Authorization': 'Bearer '+ response_data['access_token']},
                json=dict(self.order))
            test_response = client.post(
                BASE_URL+'/users/orders',
                headers={'Authorization': 'Bearer '+ response_data['access_token']},
                json=dict(self.order_input))
            self.assertEqual(test_response.status_code, 400)
    
