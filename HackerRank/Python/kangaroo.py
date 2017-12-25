#!/bin/python3

import sys

def kangaroo(x1, v1, x2, v2):
    # Complete this function
    first = x1 + v1
    second = x2 + v2
    while (first != second):
        first = first + v1
        second = second + v2

    print(first, second)
    if first == second:
        return "YES"
    else:
        return "NO"

        

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
