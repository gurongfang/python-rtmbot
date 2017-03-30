import sqlite3
from bs4 import BeautifulSoup

crontable = []
outputs = []
file_path = ''
sqlite_db = None
database_path = '/Users/gurongfang/python/flaskr/flaskr.db'

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(database_path)
    rv.row_factory = sqlite3.Row
    return rv

# @app.cli.command('initdb')
# def initdb_command():
#     """Creates the database tables."""
#     init_db()
#     print('Initialized the database.')


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    global sqlite_db
    if sqlite_db is None:
        sqlite_db= connect_db()
    return sqlite_db

def process_message(data):
    if data['channel'].startswith("D"):
        if data['text'].startswith("DE"):
            param = data['text'].split(' ')
            if len(param) < 2:
                print 'paramter error'
                return

            defect_name = param[0]
            link = param[1].replace("<","").replace(">","")
            print defect_name
            print link

            db = get_db()
            db.execute('insert into defects (title, link) values (?, ?)',
                       [defect_name, link])
            db.commit()
            outputs.append([data['channel'], 'Done! ' + defect_name + ' has completed'])

