"""
module init tests
"""

USER = {
    "username": "kabangabill",
    "email": "tkbillkabanga@gmail.com",
    "contact": "0784318356",
    "password": "0123456789",
    "role": "admin"
}
CLIENT_USER = {
    "username": "james",
    "email": "james@gmail.com",
    "contact": "0784318356",
    "password": "0123456789",
    "role": "client"
}
EMPTY_NAME = {
    "username": "       ",
    "email": "tkbillkabanga@gmail.com",
    "contact": "0784318356",
    "password": "0123456789",
    "role": "admin"
}
INVALID_ROLE = {
    "username": "kabangabill",
    "email": "tkbillkabanga@gmail.com",
    "contact": "0784318356",
    "password": "0123456789",
    "role": "whoisthis"
}
LOGIN = {
    "username": "kabangabill",
    "password": "0123456789"
}
LOGIN_CLIENT = {
    "username": "james",
    "password": "0123456789"
}
ORDER = {
    "item": "chicken",
    "price": "15000"
}
EMPTY_ITEM = {
    "item": "     ",
    "price": "15000"
}
INVALID_ITEM = {
    "item": "89798**-",
    "price": "5000"
}
ORDER_INPUT = {
    "item": "chicken",
    "quantity": "2"
}
NEW_ITEM = {
    "item": "fish",
    "quantity": "2"
}
