import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
cnt = 0


def isPrime(num):
    if(num == 1):
        return 0
    for i in range(2, num):
        if(num % i == 0):
            return 0
    return 1


for i in arr:
    if(isPrime(i) == 1):
        cnt += 1

print(cnt)
