from functools import reduce

arr = []
for i in range(3):
    arr.append(int(input()));

# 원소 곱
num = list(map(int, str(reduce(lambda x,y: x*y, arr))));

dict = {}

# 딕셔너리 초기화
for i in range(10):
    dict[i] = 0;

# 카운트 
for v in num:
    dict[v] += 1;

for i in range(10):
    print(dict[i]);
