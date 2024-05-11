#!/usr/bin/python3
def print_last_digit(number):
    fstr = repr(number)
    sign = fstr[0]
    last_no = int(fstr[-1])
    if last_no < 0 or last_no == 0:
        last_no = 0
    print("{}".format(last_no), end="")
    return(last_no)
