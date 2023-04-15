#!/usr/bin/python3
# script that takes in arguments and displays all values in the states
# table of hbtn_0e_0_usa where name matches the argument

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    list_row = cur.execute("SELECT * FROM states WHERE states.name LIKE BINARY\
                           %s ORDER BY states.id;", (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
