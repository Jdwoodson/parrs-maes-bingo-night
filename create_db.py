import os
import sqlite3
import sys

db_file = sys.argv[1]

def check_db(filename):
    return os.path.exists(filename)

if check_db(db_file):
    print('Database already exists. Exiting...')
    exit(0)

schema = '''
CREATE TABLE IF NOT EXISTS form_return(
    form_id integer PRIMARY KEY,
    full_name text,
    adults integer,
    children integer,
    cards integer,
    daubers integer,
    chicken integer
);
'''
con = sqlite3.connect(db_file)

cur = con.cursor()

cur.execute(schema)