#!/usr/bin/python3
def add_tuple(T_A=(), T_B=()):
    new_tuple = ()
    T_1 = T_A + (0, 0)
    T_2 = T_B + (0, 0)
    new_tuple = T_1[0] + T_2[0], T_1[1] + T_2[1]
    return new_tuple
