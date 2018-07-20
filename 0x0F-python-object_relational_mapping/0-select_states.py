#!/usr/bin/python3
"""
This script will list all the states from the database hbtn_0e_0usa
Passing 3 arguments:
- A mysql username
- A mysql password
- A database name

Script will return states.id in ascending order
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = database.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    for row in cur.fetchall():
        print(row)

    cur.close()
    database.close()
