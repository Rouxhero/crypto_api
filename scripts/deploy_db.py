"Database deployement scripts"

import sqlite3
from collections import namedtuple
Table = namedtuple('Table', ['name', 'columns'])
Column = namedtuple('Column', ['name', 'type', 'nullable'])
Database = namedtuple('Database', ['name', 'tables'])

def create_table(cursor, table):
    columns = ', '.join([f'{col.name} {col.type} {col.nullable}' for col in table.columns])
    cursor.execute(f'CREATE TABLE {table.name} ({columns})')

def create_database(cursor, database):
    for table in database.tables:
        create_table(cursor, table)

def main():
    db = Database('mydb', [
        Table('users', [
            Column('id', 'INTEGER', 'PRIMARY KEY'),
            Column('name', 'TEXT', 'NOT NULL'),
            Column('email', 'TEXT', 'NOT NULL'),
            Column('password', 'TEXT', 'NOT NULL'),
        ]),
        Table('posts', [
            Column('id', 'INTEGER', 'PRIMARY KEY'),
            Column('title', 'TEXT', 'NOT NULL'),
            Column('content', 'TEXT', 'NOT NULL'),
            Column('user_id', 'INTEGER', 'NOT NULL'),
        ]),
    ])
    conn = sqlite3.connect('./db/database.db')
    cursor = conn.cursor()
    create_database(cursor, db)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()