#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
exe = 0
if number < 0:
    number *= -1
    exe = 1
last_digit = number % 10
if exe == 1:
    number *= -1
    last_digit *= -1
print(f"Last digit of {number:d} is ", end="")
if last_digit > 5:
    print(f"{last_digit:d} and is greater than 5")
elif last_digit == 0:
    print(f"{last_digit:d} and is 0")
else:
    print(f"{last_digit:d} and is less than 6 and not 0")
