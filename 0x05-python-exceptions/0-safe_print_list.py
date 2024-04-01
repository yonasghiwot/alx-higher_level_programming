#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list.
    All elements must be printed on the same line followed by a new line
    x represents the number of elements to print.
    x can be bigger than the length of my_list
    You have to use try: / except:
    You are not allowed to import any module
    You are not allowed to use len()
        Args:
            my_list: list
            x: number of elements to print.
        Returns: the real number of elements printed.
    """
    number_elements = 0
    for item in range(x):
        try:
            print(my_list[item], end='')
        except IndexError:
            break
        else:
            number_elements += 1
    print()
    return number_elements
