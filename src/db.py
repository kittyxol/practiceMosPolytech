import sqlite3


def get_db_connection():
    conn = sqlite3.connect('schedule.db')
    conn.row_factory = sqlite3.Row  
    return conn


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS classes (
        id INTEGER PRIMARY KEY,
        chat_id TEXT NOT NULL,
        day TEXT NOT NULL,
        name TEXT NOT NULL,
        time TEXT NOT NULL,
        notify INTEGER NOT NULL
    )
    ''')
    conn.commit()
    conn.close()


def add_class(chat_id, day, name, time, notify):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO classes (chat_id, day, name, time, notify) VALUES (?, ?, ?, ?, ?)
    ''', (chat_id, day, name, time, notify))
    conn.commit()
    conn.close()


def get_schedule(chat_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM classes WHERE chat_id = ?
    ''', (chat_id,))
    rows = cursor.fetchall()
    conn.close()
    return rows


def clear_schedule(chat_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    DELETE FROM classes WHERE chat_id = ?
    ''', (chat_id,))
    conn.commit()
    conn.close()