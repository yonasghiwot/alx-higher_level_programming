#!/usr/bin/python3
from ast import Add
from audioop import add

if __name__ == "__main__":

    from sys import argv
    arg_addition = 0

    number_of_args = len(argv)

    if number_of_args == 0:
        print(f"{arg_addition:d}")
    for argument in argv:
        if argument != argv[0]:
            arg_addition += int(argument)

    print("{}".format(arg_addition))
