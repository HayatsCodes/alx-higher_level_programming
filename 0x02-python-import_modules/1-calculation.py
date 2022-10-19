#!/usr/bin/python3
# 1-calculation.py

if __name__ == "__main__":
    """Imports calculator_1, use its functions to do some maths,
       then prints the results.
    """
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
