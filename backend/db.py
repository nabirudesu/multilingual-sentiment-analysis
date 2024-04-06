import sqlite3
def create_connection():
 connection = sqlite3.connect("Comments.db")
 return connection

def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Comments (
    comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    campaign_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    sentiment TEXT NOT NULL
    )
    """)
    connection.commit()
    connection.close()
create_table()