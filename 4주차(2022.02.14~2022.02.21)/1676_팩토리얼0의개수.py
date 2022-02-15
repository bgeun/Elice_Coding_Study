import sys
input = sys.stdin.readline

n = int(input())
fac = 1
cnt = 0

for i in range(1, n+1):
    fac *= i

fac = str(fac)[::-1]

for i in fac:
    if i == '0':
        cnt += 1
    else:
        break

print(cnt)
