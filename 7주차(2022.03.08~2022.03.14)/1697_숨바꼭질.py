from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
MAX = 100000
visited = [False] * (MAX + 1)
dist = [0] * (MAX + 1)


def bfs():
    queue = deque([N])
    visited[N] = True

    while queue:
        x = queue.popleft()
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= MAX and not visited[nx]:
                queue.append(nx)
                visited[nx] = True
                dist[nx] = dist[x] + 1


bfs()
print(dist[K])
