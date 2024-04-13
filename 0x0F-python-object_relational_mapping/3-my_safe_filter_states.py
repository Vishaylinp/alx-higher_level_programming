#!/usr/bin/python3
"""SQL Injection"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", user=sys.argv[1], passwd=sys.argv[2],
        db =sys.argv[3], port=3306)

    cur = db.cursor()
    ver = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (ver, ))

    res = cur.fetchall()
    for row in res:
        print(row)
    cur.close()
    db.close()
