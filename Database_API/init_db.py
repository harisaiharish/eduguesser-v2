import sqlite3
from pathlib import Path

#print(__file__)

db = Path(__file__).with_name("database.db") #Fixes Issue with Relative Paths on different systems
sql = Path(__file__).with_name("schema.sql")

conn = sqlite3.connect(db)

with open(sql) as f:
    conn.executescript(f.read())

conn.commit()
conn.close()
