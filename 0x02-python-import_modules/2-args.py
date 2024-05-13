#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argv = sys.argv
    long = len(argv) - 1
    if long == 0:
        print("{} arguments.".format(long))
    elif long == 1:
        print("{} argument:".format(long))
    else:
        print("{} arguments:".format(long))
    for i in range(long):
        print("{}: {}".format(i + 1, argv[i + 1]))
