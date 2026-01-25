#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the given argument
"""
import MySQLdb
import sys


if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_pass = sys.argv[2]
    db_name = sys.argv[3]
    search_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_pass,
        db=db_name
    )

    cur = db.cursor()

    query = "SELECT * FROM states"
    "WHERE name = '{}' "
    "ORDER BY id ASC"
    .format(search_name)
    
    cur.execute(query)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
