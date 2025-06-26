from webbrowser import Error
from dal.MySqlConnection import MySQLConnection


class DalCrud:

    def __init__(self,host, user, password, database):
        self.db_config = {
            "host": host,
            "user": user,
            "password": password,
            "database": database
        }

    def select(self,query,params=None):
        try:
            with MySQLConnection(**self.db_config) as connection:
                connection.cursor.execute(query,params)
                return connection.cursor.fetchall()
        except Error as e:
            print(f"SELECT Error: {e}")
            return None

    def insert(self,query,params=None):
        try:
            with MySQLConnection(**self.db_config) as connection:
                connection.cursor.execute(query,params)
                connection.conn.commit()
                print(f"Insert successful. ")
                return connection.cursor.lastrowid
        except Error as err:
            print(f"Insert Error: {err}")
            return None

    def update(self,query, params=None):
        try:
            with MySQLConnection(**self.db_config) as connection:
                connection.cursor.execute(query, params)
                connection.conn.commit()
                print("Update successful")
                return connection.cursor.rowcount
        except Error as err:
            print(f"Update Error: {err}")
            return 0

    def delete(self, query, params=None):
        try:
            with MySQLConnection(**self.db_config) as connection:
                connection.cursor.execute(query, params)
                connection.conn.commit()
                print("Delete successful")
                return connection.cursor.rowcount
        except Error as err:
            print(f"Delete Error: {err}")
            return 0