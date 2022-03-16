import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
A, B = map(int, input().split())

cnt = N

for i in arr:
    i -= A
    if i > 0:
        if i % B > 0:
            cnt += (i // B) + 1
        else:
            cnt += i // B

print(cnt)
