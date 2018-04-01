n = int(input())
s = 'chef'
c = 0
while n > 0:
    n = n - 1
    k = 0
    s1 = input()
    if len(s1) >= 2:
        for i in range(len(s1) - 1):
            if i != len(s1) - 2:
                if s1[i:i + 2] in s:
                    # print(s1[i:i+2])
                    c = c + 1
                    k = 1
                    break
            else:
                if s1[i:] in s:
                    # print(s1[i:])
                    c = c + 1
                    k = 1
                    break
        if n < 0:
            break
        if k == 1:
            continue
print(c)
