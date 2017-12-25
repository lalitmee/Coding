#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

appleRange = 0
appleCount = []
orangeRange = 0
orangeCount = []

for i in apple:
    appleRange = a + i
    if (appleRange >= s and appleRange <= t):
        appleCount.append(appleRange)

for j in orange:
    orangeRange = b + j
    if (orangeRange >= s and orangeRange <= t):
        orangeCount.append(orangeRange)

print(len(appleCount))
print(len(orangeCount))
