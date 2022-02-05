n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

bulk = []

for i in arr:
    cnt = 1
    for j in arr:
        if i[0] < j[0] and i[1] < j[1]:
            cnt += 1
    bulk.append(cnt)

for i in bulk:
    print(i, end=" ")
