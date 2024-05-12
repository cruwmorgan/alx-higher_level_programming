#!/usr/bin/python3
for i in range(10):
    for y in range(i + 1, 10):
        if i != y:
            if (i * 10 + y) == 89:
                print("{:02}".format(89), end="")
            else:
                print("{:02}".format(i * 10 + y), end=", ")
print("")
