"""
module usermodel
"""
import re
from flask import make_response, jsonify, current_app as app
from .dbcontroller import Dbcontroller

class Users:
    """
    class for users model
    """
    def __init__(self, username, email, contact, password, role):
        """
        constructor method for users model class
        """
        self.username = username
        self.email = email
        self.contact = contact
        self.password = password
        self.role = role
    def save_user(self):
        """
        method saves new user to the database
        """
        query = "INSERT INTO users(username, email, contact, password, role)\
        VALUES('{}','{}','{}','{}','{}')RETURNING usrid"\
        .format(self.username, self.email, self.contact, self.password, self.role)
        new_db = Dbcontroller(app.config['DATABASE_URL'])
        return new_db.post_data(query)
    def get_user(self):
        """
        method gets user from database
        """
        query = "SELECT * FROM users WHERE username = '{}'".format(self.username)
        new_db = Dbcontroller(app.config['DATABASE_URL'])
        return new_db.get_data(query)
    @staticmethod
    def get_admin(username):
        """
        method gets admin user from database
        """
        query = "SELECT * FROM users WHERE username = '{}' AND role = 'admin'".format(username)
        new_db = Dbcontroller(app.config['DATABASE_URL'])
        return new_db.get_data(query)
    @staticmethod
    def validate_user_reg(username, email, contact, password, role):
        """
        method validates user attributes at registration
        """
        roles = ("admin", "client")
        if username.strip() == '':
            return make_response(jsonify({'message': 'Username cannot be empty'}), 400)
        if not re.match(r"^[a-zA-Z]+$", username):
            return make_response(jsonify({'message': 'Username should only have letters'}), 400)
        if not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.-]+$)", email):
            return make_response(jsonify({'message':'wrong email entry'}), 400)
        if not re.match(r"^07[015789]\d{7}$", contact):
            return make_response(jsonify({'message': 'Contact can only have 10 digits'}), 400)
        if len(password) < 8:
            return make_response(jsonify({'message':'Password should not be less that 8 characters'}), 400)
        if not role in roles:
            return make_response(jsonify({'message': 'Role can only be admin or client'}), 400)
        return True
