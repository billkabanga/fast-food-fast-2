"""
module run
"""
from api import create_app
from api.models.dbcontroller import Dbcontroller
from flask import current_app as app

app = create_app()

if __name__ == '__main__':
    DB_CONNECTION = Dbcontroller(app.config['DATABASE_URL'])
    DB_CONNECTION.create_tables()
    app.run()
