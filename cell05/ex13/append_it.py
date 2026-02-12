#!/usr/bin/env python3

import sys
import re

args = sys.argv[1:]

if not args:
    print("none")
else:
    found = False
    for word in args:
        if not re.search(r"ism$", word):
            print(f"{word}ism")
            found = True
    if not found:
        print("none")