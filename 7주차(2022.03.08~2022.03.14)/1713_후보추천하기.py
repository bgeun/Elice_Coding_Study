import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
reco = list(map(int, input().split()))

dic = {}

# 학생번호 : [추천 수, 들어온 순서]

for i in range(M):
    if reco[i] in dic:  # 사진틀에 올라가있는 후보라면 추천수 +1
        dic[reco[i]][0] += 1
    else:
        if len(dic) < N:  # 사진틀에 자리가 있다면 새로운 후보를 사진틀에 추가(추천수1, 들어온 순서 i)
            dic[reco[i]] = [1, i]
        else:  # 사진틀에 자리가 없다면 추천 수, 들어온 순서 기준 오름차순 정렬
            del_list = sorted(dic.items(), key=lambda x: (x[1][0], x[1][1]))
            # print(del_list)
            del_key = del_list[0][0]  # 정렬 후 젤 앞에 있는 요소의 후보 번호를 저장
            # print("del_key:", del_key)
            # print("dic[del_key]", dic[del_key])
            del dic[del_key]  # 제거
            dic[reco[i]] = [1, i]  # 비어있는 사진틀에 새로운 후보를 추가

result = list(dic.keys())
result.sort()
for i in result:
    print(i, end=" ")
