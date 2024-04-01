#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """function that divides element by element 2 lists.
    list_length can be bigger than the length of both lists

    Args:
        my_list_1: list 1
        my_list_2: list 2
        list_length: length of list
    Returns: new list(length = list_length)with all the divisions
    If an element is not an integer or float:
        print: wrong type
    If the division can’t be done (/0):
        print: division by 0
    If my_list_1 or my_list_2 is too short
        print: out of range
    You have to use try: / except: / finally:
        You are not allowed to import any module
    """
    new_list = []

    for item in range(list_length):
        try:
            quotient = my_list_1[item] / my_list_2[item]
        except IndexError:
            print("out of range")
            quotient = 0
        except TypeError:
            print("wrong type")
            quotient = 0
        except ZeroDivisionError:
            print("division by 0")
            quotient = 0
        finally:
            new_list.append(quotient)
    return new_list
