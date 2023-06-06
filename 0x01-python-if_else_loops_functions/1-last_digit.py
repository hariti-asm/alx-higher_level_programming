#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    MOD = number % 10
else:
    MOD = ((number * -1) % 10) * -1
MSG = "Last digit of {:d} is {:d} and is "
if number % 10 > 5:
    print(MSG.format(number, MOD) + "greater than 5")
elif number % 10 == 0:
    print(MSG.format(number, MOD) + "0")
else:
    print(MSG.format(number, MOD) + "less than 6 and not 0")
