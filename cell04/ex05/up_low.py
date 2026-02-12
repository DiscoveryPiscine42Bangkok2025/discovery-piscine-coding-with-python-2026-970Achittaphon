#!/usr/bin/env python3
import math

n = input()

for i in n:
    if i.isupper():
        print(i.lower(), end="")
    else:
        print(i.upper(), end="")
print()