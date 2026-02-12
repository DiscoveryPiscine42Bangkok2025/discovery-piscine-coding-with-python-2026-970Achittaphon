#!/usr/bin/env python3

import sys

count = len(sys.argv) - 1


if (count == 2):
    arr = list(range(int(sys.argv[1]), int(sys.argv[2])+1))
    print(arr)
else:
    print("none")