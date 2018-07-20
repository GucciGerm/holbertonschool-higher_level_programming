#!/usr/bin/python3

"""

"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = database.cursor()

    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY states.id\
    ASC", (argv[4],))

    for row in cur.fetchall():
        print(row)

    cur.close()
    database.close()
