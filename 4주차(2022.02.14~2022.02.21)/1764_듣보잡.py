import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = []
n_dic = {}


for i in range(n):
    x = input().rstrip()
    if x not in n_dic:
        n_dic[x] = i

for i in range(m):
    x = input().rstrip()
    if x in n_dic:
        result.append(x)

result.sort()
print(len(result))
for i in result:
    print(i)
