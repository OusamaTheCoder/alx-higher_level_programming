#!/usr/bin/python3
def uppercase(s):
    for char in s:
        ascii_value = ord(char)
        if 97 <= ascii_value <= 122:
            uppercase_char = chr(ascii_value - 32)
        else:
            uppercase_char = char
        print("{:c}".format(uppercase_char), end="")
    print()
