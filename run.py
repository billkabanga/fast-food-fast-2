"""
module run
"""
from api import create_app
from dbcontroller import Dbcontroller

APP = create_app()

if __name__ == '__main__':
    DB_CONNECTION = Dbcontroller(APP.config['DATABASE_URL'])
    DB_CONNECTION.create_tables()
    APP.run()
