#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argv = sys.argv
    long = len(argv)
    if long <= 1:
        print("{} arguments.".format(long - 1))
    else:
        print("{} arguments.".format(long - 1))
    for i in range(long - 1):
        print("{}: {}".format(i + 1, argv[i + 1]))
