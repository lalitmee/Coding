newArr = []
newObj = {}
arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]

for i in range(0, len(arr)):
    if arr[i] in newArr:
        print(newArr)
        print(newObj)
        newObj[i].append((arr[i], arr.count(i)))
    else:
        newArr.append(arr[i])
        print(newArr)
        print(newObj)
        newObj[i] = [(arr[i], arr.count(i))]
