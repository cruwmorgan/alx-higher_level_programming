#!/usr/bin/python3
def print_last_digit(number):
    fstr = repr(number)
    sign = fstr[0]
    last_no = int(fstr[-1])
    print("{}".format(last_no), end="")
    return (last_no)
