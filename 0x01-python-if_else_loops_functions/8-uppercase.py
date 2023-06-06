#!/usr/bin/python3
def uppercase(str):
    new = ""
    for X in str:
        if ord(X) >= 97 and ord(X) <= 122:
            new += chr(ord(X) - 32)
        else:
            new += X
    print("{:s}".format(new))
