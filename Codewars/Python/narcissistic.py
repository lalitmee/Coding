def narcissistic( value ):
    newValueArray = [int(i) for i in str(value)]
    lengthOfArray = len(newValueArray)
    sum = 0
    for i in range(lengthOfArray):
        sum = sum + newValueArray[i]**lengthOfArray

    if (sum == value):
        return True
    else:
        return False

