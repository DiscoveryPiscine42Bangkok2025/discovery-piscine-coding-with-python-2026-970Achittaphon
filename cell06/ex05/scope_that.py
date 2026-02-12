#!/usr/bin/env python3

import sys

def add_one(n):
    n = n + 1
    return
    
count = len(sys.argv)

if (count > 1):
    print("Does not take any parameters.")
else:
    n = 42
    add_one(n)
    print(n)