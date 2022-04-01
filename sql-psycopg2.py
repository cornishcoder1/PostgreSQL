import psycopg2

# Connect to Chinook database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table
#cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only the "Name" column from the "Artist" table
#cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only "Queen" from the "Artist" table
#cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - select only by "ArtistId" #51 from the "Artist" table
#cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
#cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])



# Query 7 - select only "Gerald Moore" from the "Artist" table
#cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Gerald Moore"])

# Query 8 - select only by "ArtistId" #270 from the "Artist" table
#cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [270])

# Query 9 - select only the albums with "ArtistId" #270 on the "Album" table
#cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [270])

# Query 10 - select all tracks where the composer is "The Postal Service" from the "Track" table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["The Postal Service"])

# Query 11 - select all records from the "Track" table
#cursor.execute('SELECT * FROM "Track"')

# Fetch the results (multiple)
results = cursor.fetchall()

#Fetch the result (single)

#results = cursor.fetchone()

#close the connection
connection.close()

#print results
for result in results:
    print(result)
