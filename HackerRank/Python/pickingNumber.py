N = int(input())

arr = list(map(int, input().split()))

arr.sort()
ans = 0

for i in range(N):
    for j in range(N):
        if abs(arr[j] - arr[i] <= 1):
            ans = max(ans, j - i + 1)
            # print(ans)

print(ans)

