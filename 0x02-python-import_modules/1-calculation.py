#!/usr/bin/python3

if __name__ == "__main__":
    """
        program that imports functions from the file calculator_1.py,
        does some Maths, and prints the result.
    """
    import calculator_1 as mycalc
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, mycalc.add(a, b)))
    print("{} - {} = {}".format(a, b, mycalc.sub(a, b)))
    print("{} * {} = {}".format(a, b, mycalc.mul(a, b)))
    print("{} / {} = {}".format(a, b, mycalc.div(a, b)))
