import sys
input = sys.stdin.readline

n = int(input())
n_card = list(map(int, input().split()))
m = int(input())
m_card = list(map(int, input().split()))

dic = {}

for i in n_card:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

for i in m_card:
    if i in dic:
        print(dic[i], end=" ")
    else:
        print(0, end=" ")
