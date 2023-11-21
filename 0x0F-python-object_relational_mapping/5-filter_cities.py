#!/usr/bin/python3
"""script that takes in the name of a state as an
argument and lists all cities of that state, using the
database hbtn_0e_4_usa"""


import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost", user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3],
            port=3306)

    cur = db.cursor()
    cur.execute("SELECT name FROM cities\
            WHERE state_id IN \
            (SELECT id FROM states WHERE name = BINARY %s) \
            ORDER BY id ASC", (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        for item in row:
            print("{}".format(item), end="")
        if row != rows[len(rows) - 1]:
            print(", ", end="")

    print("")
    cur.close()
    db.close()
