import sys

input = sys.stdin.readline

n, m = map(int, input().split())

name_arr = [input().rstrip() for i in range(n)]
problem_arr = [input().rstrip() for i in range(m)]

name_dic = {}

for i in range(n):
    name_dic[i + 1] = name_arr[i]

for i in problem_arr:
    if i.isdigit():
        print(name_dic[int(i)])
    else:
        print(name_arr.index(i) + 1)
