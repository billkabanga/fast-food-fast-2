"""
module userview
"""
from flask import jsonify, Blueprint, make_response, current_app as app
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import (create_access_token,jwt_required)
from werkzeug.security import safe_str_cmp
from api.models.usermodel import Users
from dbcontroller import Dbcontroller

user_blue_print = Blueprint('users_bp', __name__, url_prefix='/api/v1')
api = Api(user_blue_print)

class RegisterUser(Resource):
    """
    class view registers user
    """
    def __init__(self):
        """
        constructor method for the RegisterUser class 
        """
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'username',
            type=str,
            required=True,
            help='Username not given')
        self.reqparse.add_argument(
            'email',
            type=str,
            required=True,
            help='email not given')
        self.reqparse.add_argument(
            'contact',
            type=str,
            required=True,
            help='Contact not given')
        self.reqparse.add_argument(
            'password',
            type=str,
            required=True,
            help='Password not given')
        self.reqparse.add_argument(
            'role',
            type=str,
            required=True,
            help='role of user not given')
    def post(self):
        """
        method for post request
        registers new user
        """
        args = self.reqparse.parse_args()
        valid_data = Users.validate_user_reg(args['username'], args['email'],\
        args['contact'], args['password'], args['role'])
        if valid_data == True:
            name = args['username'].strip()
            response = Users(name, args['email'],\
            args['contact'], args['password'], args['role'])
            query = "SELECT * FROM users WHERE username = '{}' OR email= '{}'".format(args['username'],args['email'])
            new_db = Dbcontroller(app.config['DATABASE_URL'])
            exist = new_db.get_data(query)
            if exist:
                return make_response(jsonify({'message': 'User already exists'}), 400)
            if response.save_user():
                return make_response(jsonify({'message': 'new user registered'}), 201)
        return valid_data

class LoginUser(Resource):
    """
    class logs in registred user
    """
    def __init__(self):
        """
        constructor method for login class
        """
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'username',
            type=str,
            required=True,
            help='Username not given')
        self.reqparse.add_argument(
            'email',
            type=str,
            required=False,
            help='email not given')
        self.reqparse.add_argument(
            'contact',
            type=str,
            required=False,
            help='Contact not given')
        self.reqparse.add_argument(
            'password',
            type=str,
            required=True,
            help='Password not given')
        self.reqparse.add_argument(
            'role',
            type=str,
            required=False,
            help='role of user not given')
    def post(self):
        """
        method logs in user
        """
        args = self.reqparse.parse_args()
        response = Users(args['username'], args['email'],\
        args['contact'], args['password'], args['role'])
        user = response.get_user()
        if user and safe_str_cmp(user[4], args['password']):
            access_token = create_access_token(identity=user[1], fresh=True)
            return make_response(jsonify({'message': 'Logged in successfully', 'access_token': access_token}), 200)
        return make_response(jsonify({'message':'User not found'}), 404)

api.add_resource(RegisterUser, '/auth/signup')
api.add_resource(LoginUser, '/auth/login')
