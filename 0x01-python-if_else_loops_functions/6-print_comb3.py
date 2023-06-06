#!/usr/bin/python3
for x in range(0, 9):
    y = x + 1
    while y <= 9:
        print("{:d}{:d}".format(x, y), end='')
        print(end='\n' if x == 8 else ", ")
        y += 1
