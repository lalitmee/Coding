#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))

sumOfArr = sum(arr)

print (sumOfArr-(max(arr)), sumOfArr-(min(arr)))
