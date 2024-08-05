import sqlite3

def create_tables():
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    
    # Foydalanuvchilar jadvali
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        first_name TEXT,
        last_name TEXT,
        added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # Reklama jadvali (qolgan qismi reklama uchun)
    connection = sqlite3.connect('advertisements.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS advertisements (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT,
        media_type TEXT,
        media_file TEXT
    )
    ''')
    
    connection.commit()
    connection.close()

create_tables()


import datetime
import sqlite3

def get_users_last_24_hours():
    now = datetime.datetime.now()
    past_24_hours = now - datetime.timedelta(hours=24)
    past_24_hours_str = past_24_hours.isoformat()  # ISO 8601 formatiga o'zgartirish
    
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute('SELECT COUNT(*) FROM users WHERE added_at > ?', (past_24_hours_str,))
    count = cursor.fetchone()[0]
    connection.close()
    return count
