import sys
import copy
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
queue = deque()
result = 0


def bfs():
    global result
    lab = copy.deepcopy(arr)
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 2:
                queue.append([i, j])  # 바이러스가 있는 곳 저장

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if lab[nx][ny] == 0:
                    lab[nx][ny] = 2
                    queue.append([nx, ny])

    cnt = 0
    for i in lab:
        cnt += i.count(0)
    result = max(result, cnt)


def setWall(x):
    if x == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                setWall(x + 1)
                arr[i][j] = 0


setWall(0)
print(result)
