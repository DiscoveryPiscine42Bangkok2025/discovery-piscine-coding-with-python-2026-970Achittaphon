#!/usr/bin/env python3

print("Enter the first number:")
first_n = int(input())

print("Enter the  second number:")
second_n = int(input())

multi = first_n * second_n
print(f"{first_n} X {second_n} = {multi}")

if (multi > 0):
    print("This number is positive.")
elif (multi < 0):
    print("This number is negative.")
else:
    print("This number is both positive and negative.")