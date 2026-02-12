#!/usr/bin/env python3

str = input("Give me a number: ")
n = float(str)

if n.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")