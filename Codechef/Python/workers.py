N = int(input())

C = list(map(int, input().split()))
A = list(map(int, input().split()))

translator = 1
author = 2
author_translator = 3

trArr = []
auArr = []
atArr = []
for c in range(len(C)):
    for a in range(len(A)):
        if A[a] == translator:
            trArr.append(C[a])
        elif A[a] == author:
            auArr.append(C[a])
        else:
            atArr.append(C[a])
tr = min(set( trArr ))
au = min(set( auArr ))
at = min(set( atArr ))

if (tr + au) < at:
    print(tr + au)
elif (tr + au) == at:
    print(at)
else:
    print(at)
