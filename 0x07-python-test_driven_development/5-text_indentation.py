#!/usr/bin/python3
"""Defines a text indentation function"""


def text_indentation(text):
    """Print after each of these characters: ., ? and :"""

    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in ".?:":
        list = text.split(i)
        text = ""
        for j in list:
            text += j.strip(" ")
            if j is not list[-1]:
                text += i + "\n\n"
    print(text, end="")
