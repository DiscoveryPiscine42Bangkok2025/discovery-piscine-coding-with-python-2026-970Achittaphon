#!/usr/bin/env python3

print("Enter a number less than 25")

n = int(input())

if (n > 25):
    print("Error")
else:
    for i in range(25-(n-1)):
        print("Inside the loop, my variable is " + str(n+i))