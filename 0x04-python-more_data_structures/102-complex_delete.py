#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for i in list(a_dictionary.keys()):
        if value == a_dictionary.get(i):
            del a_dictionary[i]
    return (a_dictionary)
