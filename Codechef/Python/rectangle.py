import sys
# import collections

for i in range(int(input())):
    sides = list(map(int, input().strip().split(' ')))
    oldSum = sum(sides)
    print(oldSum)

    new  = list(set(sides))
    newSum = sum(new)

    if (2*(newSum) == oldSum):
        print("YES")
    else:
        print("NO")


