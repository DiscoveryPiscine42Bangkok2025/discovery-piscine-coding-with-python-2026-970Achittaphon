#!/usr/bin/env python3

import sys

count = len(sys.argv) - 1

if (count == 1):
    n = sys.argv[1].count('z')
    if (n > 0):
        print(n*'z')
    else:
        print("none")
else:
    print("none")