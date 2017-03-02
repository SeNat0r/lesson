import sqlite3

SQL_SELECT = '''
    SELECT
        id, short_url, original_url, created
    FROM
        shortener
'''

def dict_factory(cursor, row):
    d = {}
    for i, col in enumerate(cursor.description):
        d[col[0]] = row[i]
    return d

def connect(db_name=None):
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)
    conn.row_factory = dict_factory

    return conn

def initialize(conn):
    # cursor = conn.cursor()
    # result = cursor.execute('''SQL''')
    # cursor.commit()
    with conn:
        # cursor = conn.execute('''SQL''')
        cursor = conn.executescript('''
            CREATE TABLE IF NOT EXISTS shortener (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                short_url TEXT NOT NULL DEFAULT '',
                original_url TEXT NOT NULL,
                created DATE TIME NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        ''')

def add_url(conn, url, domain=''):
    url = url.strip('/')

    if not url:
        pass

    cursor = conn.execute('''
        INSERT INTO shortener (original_url) VALUES ( ? )
    ''', (url,))

    # хитрая логика
    pk = cursor.lastrowid
    short_url = ''

    conn.execute('''
        UPDATE shortiner SET short_url=? WHERE id=?
    ''', (short_url, pk))
    return short_url

def find_all(conn):
    with conn:
        cursor = conn.execute(SQL_SELECT)
        return cursor.fetchall

def find_url_by_pk(conn, pk):
    with conn:
        cursor = conn.execute(SQL_SELECT + ' WHERE id = ?', (pk,))
    return cursor.fetchone()

def find_url_by_short(conn, short_url):
    pass

def find_url_by_origin(conn, original_url):
    original_url = original_url.strip('/')

    with conn:
        cursor = conn.execute(SQL_SELECT + ' WHERE original_url = ?', (original_url,))
        return  cursor.fetchone()