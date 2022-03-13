import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
reco = list(map(int, input().split()))

dic = {}

for i in range(M):
    if reco[i] in dic:
        dic[reco[i]][0] += 1
    else:
        if len(dic) < N:
            dic[reco[i]] = [1, i]
        else:
            del_list = sorted(dic.items(), key=lambda x: (x[1][0], x[1][1]))
            print(del_list)
            del_key = del_list[0][0]
            del dic[del_key]
            dic[reco[i]] = [1, i]
