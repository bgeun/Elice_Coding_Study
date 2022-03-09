from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
cnt = 0

for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


for i in range(1, N + 1):
    if visited[i] == False:
        cnt += 1
        bfs(i)

print(cnt)
