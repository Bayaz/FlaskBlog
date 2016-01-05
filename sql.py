#slq.py create a sqlite3 dba nd table and populate it with data

import sqlite3

# create a new database if on doesn't already exist
with sqlite3.connect("blog.db") as connection:
	#create the cursor to input SQL 
	c = connection.cursor()

	#create the table and fields
	c.execute("""CREATE TABLE posts
			 (title TEXT,
			  post TEXT)
			  """)

	#insert dummy data into the table
	c.execute('INSERT INTO posts VALUES("Good", "I\'m good")')
	c.execute('INSERT INTO posts VALUES("Well", "I\'m well")')
	c.execute('INSERT INTO posts VALUES("Excellent", "I\'m excellent")')
	c.execute('INSERT INTO posts VALUES("Okay", "I\'m okay")')

#close database connection
c.close()