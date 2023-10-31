#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = int(repr(number)[-1])
    last_digit = last_digit*(-1)
else:
    last_digit = int(repr(number)[-1])

if last_digit > 5:
    string = "is greater than 5"
if last_digit < 6:
    string = "is less than 6 and not 0"
if last_digit == 0:
    string = "is 0"
print("Last digit of {} is {} and {}".format(number, last_digit, string))
