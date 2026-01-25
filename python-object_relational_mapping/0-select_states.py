#!/usr/bin/python3
"""
Lists all states from a database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db,
        charset="utf8"
    )

    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()
