

import sqlite3 as lite
import sys

con = None

con = lite.connect ('user.db')

with con:
	cur = (con.cursor())
	cur.execute("CREATE TABLE Users (Id INT, Name Text)")
	cur.execute("INSERT INTO Users VALUES(1, 'PRASAD')")
	cur.execute("INSERT INTO Users VALUES(2, 'SURENDRAN')")

