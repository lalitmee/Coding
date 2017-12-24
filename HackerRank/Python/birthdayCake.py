#!/bin/python3

import sys
from collections import Counter

def birthdayCakeCandles(n, ar):
    # Complete this function
    tallest = max(ar)
    occurences = Counter(ar)
    return occurences.get(tallest)



n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
