"""
module run
"""
from api import create_app
from api.models.dbcontroller import Dbcontroller
from flask import current_app as app
from config import DevelopmentConfig

app = create_app()
app.config.from_object(DevelopmentConfig)

if __name__ == '__main__':
    DB_CONNECTION = Dbcontroller(app.config['DATABASE_URL'])
    DB_CONNECTION.create_tables()
    app.run()
