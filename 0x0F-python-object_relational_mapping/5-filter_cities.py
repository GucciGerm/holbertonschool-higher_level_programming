#!/usr/bin/python3
"""
This script will take the name of a state as an argument
and we will list all the cities within that state with database hbtn_0e_4_usa
4 arguments passed:
- A MySQL username
- A MySQL password
- A database name
- A state name
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = database.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name \
    FROM cities INNER JOIN states ON cities.state_id = states.id WHERE\
    states.name = %s ORDER BY cities.id ASC", (argv[4], ))

    list = []

    for row in cur.fetchall():
        list.append(row[1])
    print(", ".join(list))

    cur.close()
    database.close()
