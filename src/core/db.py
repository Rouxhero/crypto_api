"""Database class and functions"""


import sqlite3


class DataBase:

    def __init__(self, database_path):
        self.conn = sqlite3.connect(database_path)
        self.cursor = self.conn.cursor()

    def get_users(self):
        self.cursor.execute('SELECT * FROM users')
        return self.cursor.fetchall()

    def get_user(self, name):
        self.cursor.execute('SELECT * FROM users WHERE name = ?', (name,))
        return self.cursor.fetchone()

    def create_user(self, name, email, password):
        self.cursor.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)', (name, email, password))
        self.conn.commit()


DataBaseInstance = DataBase('./db/database.db')