#!/usr/bin/python3

def multiple_returns(sentence):
    """ a function that returns a tuple with the length of
    a string and its first character

    If the sentence is empty, the first character should be equal to None
    You are not allowed to import any module
    """

    sentence_length = len(sentence)

    if sentence_length == 0:
        new_tuple = (sentence_length, None)
    else:
        new_tuple = (sentence_length, sentence[0])

    return new_tuple
