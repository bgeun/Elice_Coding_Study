import sys

input = sys.stdin.readline

N = int(input())
switch = list(map(int, input().split()))
M = int(input())

for i in range(M):
    g, s = map(int, input().split())
    if g == 1:
        for j in range(N):
            if (j + 1) % s == 0:
                switch[j] = (switch[j] + 1) % 2


print(switch)


# 남자 받은 수의 배수 스위치의 상태 바꿈
# 여자 좌우 대칭하는 구간 스위치 상태 바꿈
# 스위치의 상태를 바꿀 때 1을 더한 값에 2를 나눔
# 3 => 3 6
