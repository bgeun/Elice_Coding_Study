import sys

N = int(sys.stdin.readline())
dp = [0, 1]  # N = 0,1 일때 값 설정

for i in range(2, N + 1):
    min_value = 1e9  # 충분히 큰 수로 둠
    j = 1

    while (j**2) <= i:
        min_value = min(min_value, dp[i - (j**2)])
        j += 1
    # i까지 같거나 작은 범위에서 j값을 1씩 증가시키면서 가장 큰 유효한 제곱수를 찾는다
    dp.append(min_value + 1)

print(dp[N])
