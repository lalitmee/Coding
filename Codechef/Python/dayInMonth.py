#!/bin/python3

import sys

def daysInMonth(w, s):
    # Complete this function
    days = {"mon":4, "tues":4, "wed":4, "thurs":4, "fri":4, "sat":4, "sun":4}
    rem = int(w) % 7
    print(rem)
    if (rem == 0):
        for j in days:
            return days[j]
    else:
        for i in days:
            if (days[i] == s):
                days[i:i+(rem-1)] = days[i] + rem
                return days[i]

if __name__ == "__main__":
    t = int(input())
    for test in range(t):
        line = input().split()
        w, s = input().split(' ')
        total = daysInMonth(w, s)
        print(total)

        
