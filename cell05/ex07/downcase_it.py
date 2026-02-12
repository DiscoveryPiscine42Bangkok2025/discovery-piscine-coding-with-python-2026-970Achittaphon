#!/usr/bin/env python3

import sys


count = len(sys.argv) - 1

if (count == 1):
    print(sys.argv[1].lower())
else:
    print("none")