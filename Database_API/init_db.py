import os
import sqlite3

print(__file__)

conn = sqlite3.connect('database.db')
f = os.path.join()
with open('/Project_1A/Database_API/schema.sql') as f:
    conn.executescript(f.read())

conn.commit()
conn.close()
