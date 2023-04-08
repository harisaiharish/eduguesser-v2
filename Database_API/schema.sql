DROP TABLE IF EXISTS Locations;

CREATE TABLE Locations(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	imagePath STRING NOT NULL,
	info1 STRING NOT NULL,
	info2 STRING NOT NULL,
    info3 STRING NOT NULL,
    info4 STRING NOT NULL,
    info5 STRING NOT NULL,
    CountryName STRING NOT NULL,
    latitude STRING NOT NULL,
    longitude STRING NOT NULL
);


--SELECT column FROM table
--ORDER BY RAND ( )
--LIMIT 1

-- TOP 1 * FROM Locations order by newid()

--select newid()