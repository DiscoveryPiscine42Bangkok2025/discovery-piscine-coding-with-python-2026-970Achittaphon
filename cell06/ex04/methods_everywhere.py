#!/usr/bin/env python3

import sys

def shrink(str):
    return str[0:8]

def enlarge(str):
    while len(str) < 8:
        str = str + 'Z'  
    return str

count = len(sys.argv) - 1

if (count >= 1):
    arr = sys.argv[1:]
    for i in arr:
        if len(i) > 8:
            print(shrink(i))
        elif len(i) < 8:
            print(enlarge(i))
        else:
            print(i)
else:
    print("none")