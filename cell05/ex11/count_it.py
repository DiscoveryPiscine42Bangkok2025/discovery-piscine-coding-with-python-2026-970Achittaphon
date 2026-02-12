#!/usr/bin/env python3

import sys

count = len(sys.argv) - 1

if (count > 0):
    for i in sys.argv:
        if i == sys.argv[0]: continue
        print(f"{i}: {len(i)}")
else:
    print("none")