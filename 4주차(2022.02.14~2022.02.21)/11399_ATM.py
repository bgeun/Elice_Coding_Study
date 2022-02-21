import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

arr_sum = 0
acc = []

for i in arr:
    arr_sum += i
    acc.append(arr_sum)

print(sum(acc))
