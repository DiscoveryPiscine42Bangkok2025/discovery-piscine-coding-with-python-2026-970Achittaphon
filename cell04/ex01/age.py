#!/usr/bin/env python3

n = int(input("Please tell me your age: "))
print(f"You are currently {n} years old")

i = 10
while i < 31:
    print("In " + str(i) + " years, you'll be " + str(i+n) + " years old.")
    i+=10