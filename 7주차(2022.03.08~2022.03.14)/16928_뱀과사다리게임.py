from collections import deque
import sys

input = sys.stdin.readline

ladder = {}
snake = {}
visited = [False] * 101
board = [0] * 101
N, M = map(int, input().split())

for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y

for _ in range(M):
    x, y = map(int, input().split())
    snake[x] = y


def bfs(v):
    queue = deque([v])
    visited[v] = False
    while queue:
        x = queue.popleft()
        if x == 100:
            print(board[x])
            break
        for dice in range(1, 7):
            nx = x + dice
            if nx <= 100 and not visited[nx]:
                if nx in ladder.keys():
                    nx = ladder[nx]
                if nx in snake.keys():
                    nx = snake[nx]
                if not visited[nx]:
                    board[nx] = board[x] + 1
                    queue.append(nx)
                    visited[nx] = True


bfs(1)
