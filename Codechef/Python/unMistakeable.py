# longest number with the distinct characters

n, k = input().split()

arrOfLengths = []

for i in range(int(n)):
    string = input()
    arr = list(set(string))
    if (len(arr) <= int(k)):
        arrOfLengths.append(len(string))

if len(arrOfLengths) != 0:
    print(max(arrOfLengths))
else:
    print("-1")
