import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
S = list(input().rstrip())

cnt = 0
answer = 0
stack = []

for i in range(M):
    if S[i] == "O":
        continue
    else:
        stack.append(i)  # I의 위치 인덱스 저장

print(stack)

for i in range(1, len(stack)):
    if stack[i] - stack[i - 1] == 2:
        cnt += 1
    else:
        cnt = 0

    if cnt >= N:
        answer += 1

print(answer)
