import mysql.connector

class MySQLConnection:
    def __init__(self, host, user, password, database):
        self.config = {
            "host": host,
            "user": user,
            "password": password,
            "database": database
        }
        self.conn = None
        self.cursor = None

    def __enter__(self):
        try:
            self.conn = mysql.connector.connect(**self.config)
            self.cursor = self.conn.cursor(dictionary=True)
            return self
        except mysql.connector.Error as err:
            print(f"Connection Error: {err}")
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        if exc_type:
            print(f"Exception occurred: {exc_type} - {exc_val}")
