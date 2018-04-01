# magic elements => increase a number of the array and add all other numbers of
# array to check if the number is valid or not.

T = int(input())

for i in range(T):
    N, K =  input().split()
    A = list(map(int, input().split()))
    arraySum = sum(A)
    c = 0
    for j in range(len(A)):
        newSum = arraySum - A[j]
        eleSum = A[j] + int(K)
        if ( eleSum > newSum ):
            c += 1
        else:
            pass

    print(c)






