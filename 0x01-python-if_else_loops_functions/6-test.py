#!/usr/bin/python3
for i in range(10):
    for y in range(i + 1, 10):
        frst = repr(i)
        scnd = repr(y)
        if int(frst + scnd) == int(scnd + frst) and int(scnd + frst) == int(
               frst + scnd):
            if int(frst + scnd) <= int(scnd + frst):
                print("{:02}".format(int(frst + scnd)), end=", ")
        else:
            print("{:02}".format(int(frst + scnd), end=", "))
        if int(frst + scnd) == 89:
            print("{:02}".format(int(frst + scnd), end=" "))
