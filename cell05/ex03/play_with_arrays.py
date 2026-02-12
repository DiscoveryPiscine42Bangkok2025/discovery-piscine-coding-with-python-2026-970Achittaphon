#!/usr/bin/env python3

arr = [2, 8, 9, 48, 8, 22, -12, 2]
new_arr = []

for i in arr:
    new_arr.append(i + 2)

more_five = [i for i in new_arr if i > 5]

set_uni = set(more_five)

print(arr)
print(set_uni)