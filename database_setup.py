import sqlite3

conn = sqlite3.connect("app_data.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT
                )''')

conn.commit()
conn.close()
