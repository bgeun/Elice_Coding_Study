from collections import deque
import sys

input = sys.stdin.readline
M, N, H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
queue = deque()
result = 0
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                queue.append((i, j, k))

while queue:
    z, x, y = queue.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if -1 < nx < N and -1 < ny < M and -1 < nz < H:
            if graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                queue.append((nz, nx, ny))

for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 0:
                print(-1)
                exit()

            result = max(result, graph[i][j][k])

print(result - 1)
