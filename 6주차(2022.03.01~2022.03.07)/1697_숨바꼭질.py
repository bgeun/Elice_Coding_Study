import queue
import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
MAX = 100001
visited = [False] * (MAX + 1)
dist = [-1] * (MAX + 1)


def bfs():
    visited[n] = True
    dist[n] = 0
    queue = deque([n])

    while queue:
        x = queue.popleft()
        for nx in (x - 1, x + 1, x * 2):  # nx = 4, 6, 10
            if 0 <= nx <= MAX and not visited[nx]:
                visited[nx] = True
                dist[nx] = dist[x] + 1
                queue.append(nx)


bfs()
print(dist[k])
