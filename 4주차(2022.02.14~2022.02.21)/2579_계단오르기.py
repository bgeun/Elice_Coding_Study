import sys

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.insert(0, 0)
dp = [0] * 301

if n == 1:
    print(arr[1])
elif n == 2:
    print(arr[1] + arr[2])

else:
    dp[1] = arr[1]
    dp[2] = arr[1] + arr[2]
    dp[3] = max(arr[2] + arr[3], arr[1] + arr[3])

    for i in range(4, n + 1):
        dp[i] = max(dp[i - 3] + arr[i] + arr[i - 1], dp[i - 2] + arr[i])

    print(dp[n])

# https://daimhada.tistory.com/181
