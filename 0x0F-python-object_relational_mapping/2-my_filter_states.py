#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sat April 15 2023
@author: Okeke Morgan
"""

import MySQLdb
import sys

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 5:
        print("Usage: {} username password database_name".format(args[0]))
        exit(1)
    user = args[1]
    password = args[2]
    datab = args[3]
    state_name = args[4]
    db = MySQLdb.connect(host='localhost', user=username,
             passwd=password, db=datab, port=3306)
    cur = db.cursor()
    row_list = cur.execute("SELECT * FROM states WHERE states.name LIKE
                           BINARY\ '{}' ORDER BY states.id;".format(state_name))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
