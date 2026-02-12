#!/usr/bin/env python3

import sys

def downcase_it(str):
    return str.lower()

count = len(sys.argv) - 1

if (count >= 1):
    arr = sys.argv[1:]
    for i in arr:
        print(downcase_it(i))
else:
    print("none")


