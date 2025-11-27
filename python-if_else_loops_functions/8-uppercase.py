#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= 65 and ord(char) <= 90:
            print("{}".format(char), end="")
        else:
            print("{}".format(chr(ord(char) - 32)), end="")
