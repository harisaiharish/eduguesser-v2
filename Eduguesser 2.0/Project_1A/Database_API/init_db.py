import sqlite3

print(__file__)

conn = sqlite3.connect('database.db')

with open('schema.sql') as f:
    conn.executescript(f.read())

conn.commit()
conn.close()
