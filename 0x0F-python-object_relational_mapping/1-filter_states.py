#!/usr/bin/python3
"""
a script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    conn = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=database,
        port=3306,
        charset="utf8"
    )

    curs = conn.cursor()
    curs.execute("SELECT * FROM states WHERE name LIKE \
        'N%' ORDER BY id ASC;")
    rows = curs.fetchall()
    for row in rows:
        print(row)
