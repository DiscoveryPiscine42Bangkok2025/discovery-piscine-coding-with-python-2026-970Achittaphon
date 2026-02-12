#!/usr/bin/env python3

import sys


count = len(sys.argv) - 1

if (count > 2):
    for i in range(count):
        print(sys.argv[count - i])
else:
    print("none")