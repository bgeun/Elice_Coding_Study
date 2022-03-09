from collections import deque
import sys

input = sys.stdin.readline

T = int(input())


def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    graph[i][j] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))


for i in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for i in range(N)]
    cnt = 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(i, j)
                graph[i][j] = 0
                cnt += 1
    print(cnt)
