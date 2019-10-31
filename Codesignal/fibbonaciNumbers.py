import math

def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x

def isFibbonaciNumber(number):
    return isPerfectSquare(5*number*number + 4) or isPerfectSquare(5*number*number - 4)

def fibbonaciSum(number):
    print(number)
    total_sum = 0
    num1 = 0
    num2 = 1
    fibbonaci_numbers = []
    if isFibbonaciNumber(number) != True:
        while total_sum <= number:
            total_sum = num1 + num2
            fibbonaci_numbers.append(num2)
            fibbonaci_numbers.append(total_sum)
            num1, num2 = num2, total_sum
    print(fibbonaci_numbers)

fibbonaciSum(20)
