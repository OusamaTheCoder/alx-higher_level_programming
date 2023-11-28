#!/usr/bin/python3
def uppercase(s):
    for char in s:
        ascii = ord(char)
        if 97 <= ascii <= 122:
            uppercase_char = chr(ascii - 32)
        else:
            uppercase_char = char
        print(f"{uppercase_char}", end="")
    print()
