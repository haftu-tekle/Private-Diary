import sqlite3
import os

db_path=os.path.join(os.path.dirname(os.path.abspath(__file__), '...' 'journal.db'))
def init_db():
    connection=sqlite3.connect(db_path)

    cursor=connection.cursor()

    cursor.execute(''' CREATE TABLE IF NOT EXISTS entries(
                   Id INTEGER PRIMARY KEY AUTOINCREMENT,
                   Content TEXT,
                   Date DATETIME DEFAULT CURRENT_TIMESTAMP )
                          ''')
    connection.commit()
    connection.close()

def get_db_connection():
    return sqlite3.connect(db_path)