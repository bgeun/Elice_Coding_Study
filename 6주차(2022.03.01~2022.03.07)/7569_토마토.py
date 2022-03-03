import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())
queue = deque()
box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                queue.append((i, j, k))


def bfs():
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if -1 < nx < n and -1 < ny < m and -1 < nz < h:
                # 높이, x, y 순서
                if box[nz][nx][ny] == 0:
                    box[nz][nx][ny] = box[z][x][y] + 1
                    queue.append((nz, nx, ny))


bfs()
result = 0

for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 0:
                print(-1)
                exit()

            result = max(result, box[i][j][k])

print(result - 1)
