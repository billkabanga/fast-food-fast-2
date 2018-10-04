"""
module test_order
"""
from tests.base_test import BaseTest
from . import (ORDER, NEW_ITEM, ORDER_INPUT, ORDER_STATUS, INVALID_STATUS)

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
        self.client.post(
            BASE_URL + '/menu',
            headers={'Authorization': 'Bearer ' + self.login_admin()},
            json=dict(ORDER))
        test_response = self.client.post(
            BASE_URL + '/users/orders',
            headers={'Authorization': 'Bearer ' + self.login_client()},
            json=dict(ORDER_INPUT))
        self.assertEqual(test_response.status_code, 201)

    def test_order_not_found(self):
        """
        method tests place order where order item is not on menu
        asserts response status code is 404
        """
        self.client.post(
            BASE_URL + '/menu',
            headers={'Authorization': 'Bearer ' + self.login_admin()},
            json=dict(ORDER))
        test_response = self.client.post(
            BASE_URL + '/users/orders',
            headers={'Authorization': 'Bearer ' + self.login_client()},
            json=dict(NEW_ITEM))
        self.assertEqual(test_response.status_code, 404)

    def test_admin_not_order(self):
        """
        method tests if admin wont place order
        asserts response status code is 403
        """
        self.client.post(
            BASE_URL + '/menu',
            headers={'Authorization': 'Bearer ' + self.login_admin()},
            json=dict(ORDER))
        test_response = self.client.post(
            BASE_URL + '/users/orders',
            headers={'Authorization': 'Bearer ' + self.login_admin()},
            json=dict(ORDER_INPUT))
        self.assertEqual(test_response.status_code, 403)

    def test_get_orders(self):
        """
        method tests get orders endpoint
        asserts response status code is 200
        """
        self.client.post(
            BASE_URL + '/menu',
            headers={'Authorization': 'Bearer ' + self.login_admin()},
            json=dict(ORDER))
        self.client.post(
            BASE_URL + '/users/orders',
            headers={'Authorization': 'Bearer ' + self.login_client()},
            json=dict(ORDER_INPUT))
        test_response = self.client.get(
            BASE_URL + '/orders',
            headers={'Authorization': 'Bearer ' + self.login_admin()})
        self.assertEqual(test_response.status_code, 200)

    def test_no_orders(self):
        """
        method tests get orders endpoint where no orders are found
        asserts response status code is 404
        """
        self.client.post(
            BASE_URL + '/menu',
            headers={'Authorization': 'Bearer ' + self.login_admin()},
            json=dict(ORDER))
        test_response = self.client.get(
            BASE_URL + '/orders',
            headers={'Authorization': 'Bearer ' + self.login_admin()})
        self.assertEqual(test_response.status_code, 404)

    def test_client_not_get_orders(self):
        """
        method tests get orders endpoint where client can't get all orders
        asserts response status code is 403
        """
        self.client.post(
            BASE_URL + '/menu',
            headers={'Authorization': 'Bearer ' + self.login_admin()},
            json=dict(ORDER))
        self.client.post(
            BASE_URL + '/users/orders',
            headers={'Authorization': 'Bearer ' + self.login_client()},
            json=dict(ORDER_INPUT))
        test_response = self.client.get(
            BASE_URL + '/orders',
            headers={'Authorization': 'Bearer ' + self.login_client()})
        self.assertEqual(test_response.status_code, 403)

    def test_get_specific_order(self):
        """
        method tests get specific order endpoint
        asserts response status code is 200
        """
        self.client.post(
            BASE_URL + '/menu',
            headers={'Authorization': 'Bearer ' + self.login_admin()},
            json=dict(ORDER))
        self.client.post(
            BASE_URL + '/users/orders',
            headers={'Authorization': 'Bearer ' + self.login_client()},
            json=dict(ORDER_INPUT))
        self.client.post(
            BASE_URL + '/users/orders',
            headers={'Authorization': 'Bearer ' + self.login_client()},
            json=dict(ORDER_INPUT))
        test_response = self.client.get(
            BASE_URL + '/orders/2',
            headers={'Authorization': 'Bearer ' + self.login_admin()})
        self.assertEqual(test_response.status_code, 200)

    def test_specific_order_not_found(self):
        """
        method tests get specific order endpoint where order is not found
        asserts response status code is 404
        """
        self.client.post(
            BASE_URL + '/menu',
            headers={'Authorization': 'Bearer ' + self.login_admin()},
            json=dict(ORDER))
        self.client.post(
            BASE_URL + '/users/orders',
            headers={'Authorization': 'Bearer ' + self.login_client()},
            json=dict(ORDER_INPUT))
        self.client.post(
            BASE_URL + '/users/orders',
            headers={'Authorization': 'Bearer ' + self.login_client()},
            json=dict(ORDER_INPUT))
        test_response = self.client.get(
            BASE_URL + '/orders/100',
            headers={'Authorization': 'Bearer ' + self.login_admin()})
        self.assertEqual(test_response.status_code, 404)

    def test_update_status(self):
        """
        method tests put request for updating status
        asserts response status code is 201
        """
        self.client.post(
            BASE_URL + '/menu',
            headers={'Authorization': 'Bearer ' + self.login_admin()},
            json=dict(ORDER))
        self.client.post(
            BASE_URL + '/users/orders',
            headers={'Authorization': 'Bearer ' + self.login_client()},
            json=dict(ORDER_INPUT))
        self.client.post(
            BASE_URL + '/users/orders',
            headers={'Authorization': 'Bearer ' + self.login_client()},
            json=dict(ORDER_INPUT))
        test_response = self.client.put(
            BASE_URL + '/orders/2',
            headers={'Authorization': 'Bearer ' + self.login_admin()},
            json=dict(ORDER_STATUS))
        self.assertEqual(test_response.status_code, 201)

    def test_client_not_update_status(self):
        """
        method tests put request where client can't update status
        asserts response status code is 403
        """
        self.client.post(
            BASE_URL + '/menu',
            headers={'Authorization': 'Bearer ' + self.login_admin()},
            json=dict(ORDER))
        self.client.post(
            BASE_URL + '/users/orders',
            headers={'Authorization': 'Bearer ' + self.login_client()},
            json=dict(ORDER_INPUT))
        self.client.post(
            BASE_URL + '/users/orders',
            headers={'Authorization': 'Bearer ' + self.login_client()},
            json=dict(ORDER_INPUT))
        test_response = self.client.put(
            BASE_URL + '/orders/2',
            headers={'Authorization': 'Bearer ' + self.login_client()},
            json=dict(ORDER_STATUS))
        self.assertEqual(test_response.status_code, 403)

    def test_order_for_status_not_found(self):
        """
        method tests put request where order is not found
        asserts response status code is 404
        """
        self.client.post(
            BASE_URL + '/menu',
            headers={'Authorization': 'Bearer ' + self.login_admin()},
            json=dict(ORDER))
        self.client.post(
            BASE_URL + '/users/orders',
            headers={'Authorization': 'Bearer ' + self.login_client()},
            json=dict(ORDER_INPUT))
        self.client.post(
            BASE_URL + '/users/orders',
            headers={'Authorization': 'Bearer ' + self.login_client()},
            json=dict(ORDER_INPUT))
        test_response = self.client.put(
            BASE_URL + '/orders/*-/*-',
            headers={'Authorization': 'Bearer ' + self.login_admin()},
            json=dict(ORDER_STATUS))
        self.assertEqual(test_response.status_code, 404)

    def test_invalid_status(self):
        """
        method tests put request where input is invalid
        asserts response status code is 400
        """
        self.client.post(
            BASE_URL + '/menu',
            headers={'Authorization': 'Bearer ' + self.login_admin()},
            json=dict(ORDER))
        self.client.post(
            BASE_URL + '/users/orders',
            headers={'Authorization': 'Bearer ' + self.login_client()},
            json=dict(ORDER_INPUT))
        self.client.post(
            BASE_URL + '/users/orders',
            headers={'Authorization': 'Bearer ' + self.login_client()},
            json=dict(ORDER_INPUT))
        test_response = self.client.put(
            BASE_URL + '/orders/2',
            headers={'Authorization': 'Bearer ' + self.login_admin()},
            json=dict(INVALID_STATUS))
        self.assertEqual(test_response.status_code, 400)

    def test_get_order_history(self):
        """
        method tests get order history endpoint
        asserts response status code is 200
        """
        self.client.post(
            BASE_URL + '/menu',
            headers={'Authorization': 'Bearer ' + self.login_admin()},
            json=dict(ORDER))
        self.client.post(
            BASE_URL + '/users/orders',
            headers={'Authorization': 'Bearer ' + self.login_client()},
            json=dict(ORDER_INPUT))
        test_response = self.client.get(
            BASE_URL + '/users/orders',
            headers={'Authorization': 'Bearer ' + self.login_client()})
        self.assertEqual(test_response.status_code, 200)

    def test_no_order_history(self):
        """
        method tests get order history endpoint: no orders placed so far
        asserts response status code is 404
        """
        self.client.post(
            BASE_URL + '/menu',
            headers={'Authorization': 'Bearer ' + self.login_admin()},
            json=dict(ORDER))
        test_response = self.client.get(
            BASE_URL + '/users/orders',
            headers={'Authorization': 'Bearer ' + self.login_client()})
        self.assertEqual(test_response.status_code, 404)

    def test_admin_order_history(self):
        """
        method tests get order history endpoint: admin not order history
        asserts response status code is 403
        """
        self.client.post(
            BASE_URL + '/menu',
            headers={'Authorization': 'Bearer ' + self.login_client()},
            json=dict(ORDER))
        test_response = self.client.get(
            BASE_URL + '/users/orders',
            headers={'Authorization': 'Bearer ' + self.login_admin()})
        self.assertEqual(test_response.status_code, 403)
