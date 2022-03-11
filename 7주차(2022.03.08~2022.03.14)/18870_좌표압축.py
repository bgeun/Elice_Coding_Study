import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
sorted_arr = list(set(arr))
sorted_arr = sorted(sorted_arr)
dic = {}

for i in range(len(sorted_arr)):
    dic[sorted_arr[i]] = i

for i in arr:
    print(dic[i], end=" ")
