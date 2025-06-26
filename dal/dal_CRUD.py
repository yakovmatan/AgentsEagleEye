import mysql
from dal.MySqlConnection import MySQLConnection


class DalCrud:

    def __init__(self,connection: MySQLConnection):
        self.connection = connection

    def select(self,query,params=None):
        try:
            self.connection.cursor.execute(query,params)
            return self.connection.cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"SELECT Error: {err}")
            return []

    def insert(self,query,params=None):
        try:
            self.connection.cursor.execute(query,params)
            self.connection.conn.commit()
            print(f"Insert successful. ")
            return self.connection.cursor.lastrowid
        except mysql.connector.Error as err:
            print(f"Insert Error: {err}")
            return None

    def update(self,query, params=None):
        try:
            self.connection.cursor.execute(query, params)
            self.connection.conn.commit()
            print("Update successful")
            return self.connection.cursor.rowcount
        except mysql.connector.Error as err:
            print(f"Update Error: {err}")
            return 0

    def delete(self, query, params=None):
        try:
            self.connection.cursor.execute(query, params)
            self.connection.conn.commit()
            print("Delete successful")
            return self.connection.cursor.rowcount
        except mysql.connector.Error as err:
            print(f"Delete Error: {err}")
            return 0