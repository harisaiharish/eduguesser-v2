import sqlite3


# get connection to the database
def get_dbConn():
    conn = sqlite3.connect('database.db')
    return conn


def new_Location(imagePath, info1, info2, info3, info4, info5, CountryName, latitude, longitude):
    conn = get_dbConn()
    cur = conn.cursor()
    print("debugging heheheha")
    cmd = 'INSERT INTO Locations(imagePath, info1, info2, info3, info4, info5, CountryName, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?, ?, ?,?)'
    cur.execute(cmd, [imagePath, info1, info2, info3, info4, info5, CountryName, latitude, longitude])
    print([imagePath, info1, info2, info3, info4, info5, CountryName, latitude, longitude])
    conn.commit()
    return True


def update_Location(id, imagePath, info1, info2, info3, info4, info5, CountryName, latitude, longitude):
    conn = get_dbConn()
    cur = conn.cursor()

    cmd = 'UPDATE Locations SET imagePath = ?, info1 = ?, info2 = ?, info3 = ?, info4 = ?, info5 = ?, CountryName = ?, latitude = ?, longitude = ? WHERE id = ?'
    cur.execute(cmd, [imagePath, info1, info2, info3, info4, info5, CountryName, latitude, longitude, id])

    conn.commit()
    return True


# deletes record
def delete_Location(id):
    conn = get_dbConn()
    cur = conn.cursor()

    cmd = "DELETE FROM Locations WHERE Id = ?"
    cur.execute(cmd, [id])

    conn.commit()
    return True


# returns record of id id
def get_by_id(Id):
    conn = get_dbConn()
    cur = conn.cursor()

    cmd = "Select Id, imagePath, info1, info2, info3, info4, info5, CountryName, latitude, longitude FROM Locations WHERE Id = ?"
    cur.execute(cmd, [Id])

    return cur.fetchone()


# Returns all records
def get_Locations():
    conn = get_dbConn()
    cur = conn.cursor()

    query = "SELECT id, imagePath, info1, info2, info3, info4, info5, CountryName, latitude, longitude FROM Locations"
    cur.execute(query)

    return cur.fetchall()


def get_IDs():
    conn = get_dbConn()
    cur = conn.cursor()

    query = "SELECT id FROM Locations"
    cur.execute(query)

    return cur.fetchall()

# def get_randlLocation():
#    conn = get_dbConn()
#    cur = conn.cursor()
