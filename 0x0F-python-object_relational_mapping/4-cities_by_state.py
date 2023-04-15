#!/usr/bin/python3
# script that lists all cities from the database hbtn_0e_4_usa

import sys
import MySQLdb

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 4:
        print("Usage: {} username password database_name".format(args[0]))
        exit(1)
    username = argv[1]
    password = args[2]
    dbname = args[3]
    db = MySQLdb.connect("localhost", username, password, dbname, 3306)
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name\
                           FROM cities INNER JOIN states\
                           ON cities.state_id=states.id\
                           ORDER BY cities.id;")
    # fetch all the matching rows
    result = cursor.fetchall()
    # loop through the rows
    for row in result:
    print(row)
    cursor.close()
    db.close()
