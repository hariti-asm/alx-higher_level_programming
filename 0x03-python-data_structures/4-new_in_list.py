#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list = my_list.copy()
    if idx < 0:
        return (list)
    if idx > len(my_list) - 1:
        return (list)
    list[idx] = element
    return (list)
