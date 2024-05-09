#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
fstr = repr(number)
sign = fstr[0]
if sign == "-" and fstr[-1] != 0:
    last_no = int(fstr[0] + fstr[-1])
else:
    last_no = int(fstr[-1])

if last_no > 5:
    print("Last digit of {} is {} and is greater than 5".format(
           number, last_no
           ))
elif last_no == 0:
    print("Last digit of {} is {} and is 0".format(number, last_no))
elif last_no < 6 and last_no != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(
           number, last_no
           ))
