#!/bin/python3

for isdfrgti in range(int(input())):
    s = list(map(str, input().strip().split(' ')))
    ddd = ['mon', 'tues', 'wed', 'thurs', 'fri', 'sat', 'sun']
    for i in range(7):
        if(ddd[i] == s[1]):
            break
    f = [0 for i in range(7)]
    j = 0
    while(j < int(s[0])):
        f[i] += 1
        i = (i + 1) % 7
        j += 1
        for i in f:
            print(i, end=' ')
            print()
