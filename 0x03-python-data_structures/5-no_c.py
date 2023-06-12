#!/usr/bin/python3
def no_c(my_string):
    str_translate = {ord(i): None for i in 'cC'}
    new_string = my_string.translate(str_translate)
    return new_string
