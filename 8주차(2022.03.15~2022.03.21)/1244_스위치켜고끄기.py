import sys

input = sys.stdin.readline

N = int(input())
switch = [-1] + list(map(int, input().split()))
M = int(input())


def on_off(num):
    switch[num] = (switch[num] + 1) % 2


for i in range(M):
    gender, s = map(int, input().split())
    if gender == 1:
        for j in range(s, N + 1, s):
            on_off(j)

    else:
        on_off(s)
        for i in range(1, N // 2):
            if s + i > N or s - i < 1:
                break
            if switch[s - i] == switch[s + i]:
                on_off(s - i)
                on_off(s + i)
            else:
                break

for i in range(1, N + 1):
    print(switch[i], end=" ")
    if i % 20 == 0:
        print()

# 남자 받은 수의 배수 스위치의 상태 바꿈
# 여자 좌우 대칭하는 구간 스위치 상태 바꿈
# 스위치의 상태를 바꿀 때 1을 더한 값에 2를 나눈 나머지로 바꿈
# 3 => 3 6
