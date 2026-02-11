import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print('Connection successful')
    except Error as e:
        print(f'Error connecting to database: {e}')
    return connection

