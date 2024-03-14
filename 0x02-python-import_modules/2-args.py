#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv
    arg_count = 1

    # removes name of program
    number_of_args = len(argv) - 1
    if number_of_args == 0:
        print(f"{number_of_args:d} arguments.")
    if number_of_args == 1:
        print(f"{number_of_args:d} argument:")
    if number_of_args > 1:
        print(f"{number_of_args:d} arguments:")
    while arg_count < len(argv):
        print(f"{arg_count:d}: {argv[arg_count]}")
        arg_count += 1
