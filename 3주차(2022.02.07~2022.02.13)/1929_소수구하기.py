import math
import sys
input = sys.stdin.readline

m, n = map(int, input().split())

arr = [True] * (n + 1)

for i in range(2, int(math.sqrt(n)) + 1):
    if arr[i] == True:
        j = 2
        while i * j <= n:
            arr[i*j] = False
            j += 1

for i in range(m, n+1):
    if i > 1 and arr[i] == True:
        print(i)
