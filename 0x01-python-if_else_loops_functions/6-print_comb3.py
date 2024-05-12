#!/usr/bin/python3
for i in range(10):
    for y in range(i + 1, 10):
        if i != y:
            print("{:02}".format(i * 10 + y), end=", ")
print("{:02}".format(89))
