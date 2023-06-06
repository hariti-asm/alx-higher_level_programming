#!/usr/bin/python3
for x in range(0, 100):
    print("{:02d}".format(x), end='')
    print(end='\n' if x == 99 else ", ")
