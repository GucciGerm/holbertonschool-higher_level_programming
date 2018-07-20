#!/usr/bin/python3

"""
This script will take an argument (ex.name) and display all the values\
in the states table of the hbtn_0e_0_usa database, return matching name
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = database.cursor()

    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY states.id ASC\
    ".format(argv[4]))
    for row in cur.fetchall():
        if row[1] == argv[4]:
            print(row)

    cur.close()
    database.close()
