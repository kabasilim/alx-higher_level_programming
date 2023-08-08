#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
un_number = number

if un_number < 0:
    un_number *= -1
    last_digit = un_number % 10
    last_digit *= -1
else:
    last_digit = number % 10

if last_digit == 0:
    print(f"Last digit of {number:d} is {last_digit:d} and is 0")
elif last_digit < 6:
    print(f"Last digit of {number:d} is {last_digit:d} "
          "and is less than 6 and not 0")
else:
    print(f"Last digit of {number:d} is {last_digit:d} "
          "and is greater than 5")
