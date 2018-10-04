"""
module test_menu
"""
from tests.base_test import BaseTest

from . import (ORDER, EMPTY_ITEM, INVALID_ITEM)
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
        test_response = self.client.post(
            BASE_URL + '/menu',
            headers={'Authorization': 'Bearer ' + self.login_admin()},
            json=dict(ORDER))
        self.assertEqual(test_response.status_code, 201)

    def test_client_user_not_allowed(self):
        """
        test method for adding food item
        asserts response status is 403
        """
        test_response = self.client.post(
            BASE_URL + '/menu',
            headers={'Authorization': 'Bearer ' + self.login_client()},
            json=dict(ORDER))
        self.assertEqual(test_response.status_code, 403)

    def test_empty_food_item(self):
        """
        test method for empty food item
        asserts response status is 400
        """
        test_response = self.client.post(
            BASE_URL + '/menu',
            headers={'Authorization': 'Bearer ' + self.login_admin()},
            json=dict(EMPTY_ITEM))
        self.assertEqual(test_response.status_code, 400)

    def test_ivalid_food(self):
        """
        test method for invalid food input
        asserts response status code is 400
        """
        test_response = self.client.post(
            BASE_URL + '/menu',
            headers={'Authorization': 'Bearer ' + self.login_admin()},
            json=dict(INVALID_ITEM))
        self.assertEqual(test_response.status_code, 400)

    def test_empty_menu(self):
        """
        test method for empty menu
        asserts response status code is 404
        """
        response = self.client.get(BASE_URL + '/menu')
        self.assertEqual(response.status_code, 404)

    def test_get_menu(self):
        """
        test method for getting menu
        asserts response status code is 200
        """
        self.client.post(
            BASE_URL + '/menu',
            headers={'Authorization': 'Bearer ' + self.login_admin()},
            json=dict(ORDER))
        test_response = self.client.get(BASE_URL + '/menu')
        self.assertEqual(test_response.status_code, 200)
