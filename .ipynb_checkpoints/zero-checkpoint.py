a = [1,2,0,30,1,0,0,8]

#[1,2,30,1,8,0,0,0]

i = 0

arr1 = []
arr2 = []

for ele in a:
    if (ele != i):
        arr1.append(ele)
    else:
        arr2.append(ele)

for j in arr2:
    arr1.append(j)

print (arr1)

