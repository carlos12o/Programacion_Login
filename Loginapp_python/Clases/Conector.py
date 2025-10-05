import mysql.connector

class Conector:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="tecnar_app",
            port=3307
        )
        self.cursor = self.conn.cursor()

    def select(self, sql, values):
        self.cursor.execute(sql, values)
        return self.cursor.fetchall()

    def execute_query(self, sql, values):
        self.cursor.execute(sql, values)
        self.conn.commit()
        return self.cursor.lastrowid