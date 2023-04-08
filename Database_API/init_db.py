import os
import sqlite3

print(__file__)

conn = sqlite3.connect('database.db')

with open('Database_API/schema.sql') as f:
    conn.executescript(f.read())

conn.commit()
conn.close()
