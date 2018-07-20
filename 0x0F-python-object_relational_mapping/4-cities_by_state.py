#!/usr/bin/python3

"""
This script will list all cities from the database hbtn_0e_4_usa
3 arguments:
- username
- password
- database name
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = database.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
    INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")

    for row in cur.fetchall():
        print(row)

    cur.close()
    database.close()
