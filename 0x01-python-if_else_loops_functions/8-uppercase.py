#!/usr/bin/python3
def uppercase(s):
    separator = ""
    for char in s:
        ascii_value = ord(char)
        if 97 <= ascii_value <= 122:
            uppercase_char = chr(ascii_value - 32)
        else:
            uppercase_char = char
        print("{:s}".format(separator), end="")
        print("{:s}".format(uppercase_char), end="")
        separator = ""
    print()
