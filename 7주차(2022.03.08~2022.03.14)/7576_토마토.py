from collections import deque
import sys

input = sys.stdin.readline

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit()

    result = max(result, max(i))

print(result - 1)
