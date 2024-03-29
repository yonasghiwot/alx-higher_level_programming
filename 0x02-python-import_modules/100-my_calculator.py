#!/usr/bin/python3

if __name__ == "__main__":

    from calculator_1 import add, mul, div, sub
    from sys import argv, exit

    # removes name of file
    number_of_args = len(argv) - 1

    if number_of_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    basic_operator = argv[2]

    if basic_operator != '+' and basic_operator != '-' and basic_operator != '*' and basic_operator != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    if basic_operator == '+':
        print("{:d} {} {:d} = {}".format(a, argv[2], b, add(a, b)))
    elif basic_operator == '-':
        print("{:d} {} {:d} = {}".format(a, argv[2], b, sub(a, b)))
    elif basic_operator == '*':
        print("{:d} {} {:d} = {}".format(a, argv[2], b, mul(a, b)))
    else:
        print("{:d} {} {:d} = {}".format(a, argv[2], b, div(a, b)))
