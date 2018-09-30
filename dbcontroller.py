"""
module dbcontroller
"""
from urllib.parse import urlparse
import psycopg2

class Dbcontroller:
    """
    class handles database connection
    """
    def __init__(self, database_url):
        """
        constructor method for the class
        """
        parsed_url = urlparse(database_url)
        dbname = parsed_url.path[1:]
        user = parsed_url.username
        host = parsed_url.hostname
        password = parsed_url.password
        port = parsed_url.port
        self.conn = psycopg2.connect(
            database=dbname,
            user=user,
            password=password,
            host=host,
            port=port)
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()
    def create_tables(self):
        """
        method creates tables
        """
        user_table = "CREATE TABLE IF NOT EXISTS users(usrId serial PRIMARY KEY,\
          username varchar(50), email varchar(100),\
          contact varchar(10), password varchar(20), role varchar(15))"
        orders_table = "CREATE TABLE IF NOT EXISTS orders(orderId serial PRIMARY KEY,\
          item varchar(100), quantity integer, price integer,order_date timestamp,\
          order_status varchar(20), client varchar(50))"
        menu_table = "CREATE TABLE IF NOT EXISTS menu(menuid serial PRIMARY KEY, item varchar(100),\
          price integer)"
        self.cursor.execute(user_table)
        self.cursor.execute(orders_table)
        self.cursor.execute(menu_table)
    def drop_tables(self):
        """
        method drops tables
        """
        drop_user_table = "DROP TABLE users cascade"
        drop_orders_table = "DROP TABLE orders cascade"
        drop_menu_table = "DROP TABLE menu cascade"  
        self.cursor.execute(drop_user_table)
        self.cursor.execute(drop_orders_table)
        self.cursor.execute(drop_menu_table)
    def post_data(self, query):
        """
        method posts data to database.
        """
        self.cursor.execute(query)
        return True
    def get_data(self, query):
        """
        method gets data from database
        """
        self.cursor.execute(query)
        data = self.cursor.fetchone()
        return data
    def get_all_data(self, query):
        """
        method gets all data from database
        """
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        return data
    def delete_data(self, query):
        """
        method deletes data from database
        """
        self.cursor.execute(query)
        return True
    