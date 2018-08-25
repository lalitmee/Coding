def filter_list(l):
    sampleString = ''
    sampleType = type(sampleString)
    newArr = []
    for i in range(len(l)):
        if type(l[i]) != sampleType:
            newArr.append(l[i])
        else:
            pass
    print(newArr)
    return newArr

filter_list([1,2,'aasf','1','123',123])

