import sys

input = sys.stdin.readline

n, m = map(int, input().split())
result = []
n_dic = {}

for i in range(n):
    x = input().rstrip().split()
    n_dic[x[0]] = x[1]

for i in range(m):
    x = input().rstrip()
    if x in n_dic:
        result.append(n_dic[x])

for i in result:
    print(i)
