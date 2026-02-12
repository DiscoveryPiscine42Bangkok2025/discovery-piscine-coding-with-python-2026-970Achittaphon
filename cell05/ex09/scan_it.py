#!/usr/bin/env python3

import sys

count = len(sys.argv) - 1

if (count == 2):
    search = sys.argv[1]
    text = sys.argv[2]

    n = text.count(search)
    print(n)
else:
    print("none")
