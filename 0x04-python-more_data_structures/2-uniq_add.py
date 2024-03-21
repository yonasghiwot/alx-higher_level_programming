#!/usr/bin/python3

def uniq_add(my_list=[]):

    """func adds all unique integers in a list (only once for each integer)
    You are not allowed to import any module
    """

    new_list = list(set(my_list))
    result = 0

    for num in new_list:
        result += num
    return result
