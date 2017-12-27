#!/bin/python3

import sys

def getRecord(s):
    # Complete this function
    maxCount = 0
    minCount = 0
    maxScore = minScore = s[0]
     
    # print(score)
    for i in s:
        if i < minScore:
            minCount += 1
            minScore = i

        elif i > maxScore:
            maxCount += 1
            maxScore = i

    return maxCount, minCount

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))
