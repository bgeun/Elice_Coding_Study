from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = []


def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    graph[i][j] = 0
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                cnt += 1
                queue.append((nx, ny))

    return cnt


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            result.append(bfs(i, j))

result.sort()
print(len(result))
for i in result:
    print(i)
