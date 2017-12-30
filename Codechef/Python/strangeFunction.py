#!/bin/python3

import sys

def strangeFunction(a, n):
    # Complete this function
    if (n > 1):
        mult = a**n
        multArr = [int(i) for i in str(mult)]
        if (len(multArr) > 1):
            #print(len(multArr))
            return sumArr(multArr)
        else:
            return mult

    elif (n == 1):
        lessOne = [int(i) for i in str(a)]
        if (len(lessOne) > 1):
            return sumArr(lessOne)
        else:
            return a
        

def sumArr(multArr):
    sum = 0
    for ele in multArr:
        sum = sum + ele

    arrSum = [int(j) for j in str(sum)]
    if (len(arrSum)> 1):
        #print(len(arrSum))
        return sumArr(arrSum)
    else:
        return sum


if __name__ == "__main__":
    t = int(input())
    if (t >= 1 and t <= 10**5):
        for test in range(t):    
            a, n = map(int, input().split(' '))
            if ( a >= 1 and a <= 10**18) and (n >= 1 and n <= 10**18):
                A = a % 10**14
                N = n % 10**14
                total = strangeFunction(A, N)
                print(total)

            elif ( a >= 1 and a <= 10**5) and (n >= 1 and n <= 3):
                A = a 
                N = n
                total = strangeFunction(A, N)
                print(total)

            elif ( a >= 1 and a <= 10**5) and (n >= 1 and n <= 100):
                A = a % 10**3
                N = n % 10**2
                total = strangeFunction(A, N)
                print(total)


    else:
        pass

