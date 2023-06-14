#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    for i in list(a_dictionary.keys()):
        new_dictionary[i] *= 2
    return new_dictionary
