#!/usr/bin/python3
"""
 takes in a URL, sends a request
 to the URL and displays the value of the X-Request-Id
 variable found
"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        print(response.getheader("X-Request-Id"))
