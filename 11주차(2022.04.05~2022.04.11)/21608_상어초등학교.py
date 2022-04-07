import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
dic = {}
seat = [[0 for _ in range(n)] for _ in range(n)]
dic = defaultdict(list)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(n * n):
    a = list(map(int, input().split()))
    student = a[0]
    like = a[1:]
    dic[student] = like

for student, like in dic.items():
    tmp = []
    for i in range(n):
        for j in range(n):
            empty = 0
            cnt = 0

            if seat[i][j] != 0:
                continue

            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue

                if seat[nx][ny] == 0:
                    empty += 1
                if seat[nx][ny] in like:
                    cnt += 1
            tmp.append([cnt, empty, i, j])
    print(tmp)
    print("-" * 20)
    tmp.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    print(tmp)
    print("-" * 20)
    seat[tmp[0][2]][tmp[0][3]] = student

print(seat)

result = 0

for i in range(n):
    for j in range(n):
        amount = 0

        for k in range(n):
            nx = i + dx[k]
            ny = j + dy[k]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if seat[nx][ny] in dic[seat[i][j]]:
                amount += 1
        print(amount)
        if amount == 0:
            result += 0
        elif amount == 1:
            result += 1
        else:
            result += 10 ** (amount - 1)

print(result)
