import sys
input = sys.stdin.readline

n = int(input())

arr = [int(input()) for _ in range(n)]

# 평균
print(round(sum(arr) / n))

# 중앙값
sorted_arr = sorted(arr)
print(sorted_arr[n//2])

# 최빈값
dic = {}
for i in arr:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

sorted_dic = sorted(dic.items(), key=lambda x: -x[1])

max_num = sorted_dic[0][1]
max_list = []

for i in sorted_dic:
    if(i[1] == max_num):
        max_list.append(i[0])


if len(max_list) >= 2:
    max_list.sort()
    print(max_list[1])
else:
    print(max_list[0])

# 범위
print(max(arr) - min(arr))
