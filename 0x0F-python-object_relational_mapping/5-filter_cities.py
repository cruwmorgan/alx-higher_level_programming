#!/usr/bin/python3
# script that takes in the name of a state as an argument and lists all cities
# of that state, using the database hbtn_0e_4_usa

import MySQLdb
import sys

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 5:
        print("Usage: {} username password database_name".format(args[0]))
        exit(1)
    username = args[1]
    password = args[2]
    dbname = args[3]
    state_name = args[4]
    db = MySQLdb.connect(host='localhost', user=username, passwd=password,
            db=dbname, port=3306)
    cursor = db.cursor()
    sql = "SELECT cities.name FROM cities WHERE state_id =\
            (SELECT id FROM states WHERE name LIKE BINARY %s)\
            ORDER BY cities.id;"
    list_row = cursor.execute(sql, (state_name, ))
    result = cursor.fetchall()
    i = 1
    for row in rows:
        print(row[0], end='')
        if i < num_rows:
            print(end=', ')
        i += 1
    print()
    cursor.close()
    db.close()
