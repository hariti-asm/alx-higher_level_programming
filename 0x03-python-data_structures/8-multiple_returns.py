#!/usr/bin/python3
def multiple_returns(sentence):
    Tuple = ()
    if sentence == "":
        first = None
    else:
        first = sentence[0]
    Tuple = len(sentence), first
    return Tuple
