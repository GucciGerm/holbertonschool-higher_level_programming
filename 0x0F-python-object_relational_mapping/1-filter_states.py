#!/usr/bin/python3
"""

"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = database.cursor()

    cur.execute("SELECT * FROM states WHERE name\
    LIKE 'N%' ORDER BY states.id ASC")
    for row in cur.fetchall():
        if row[1][0] == 'N':
            print(row)

    cur.close()
    database.close()
