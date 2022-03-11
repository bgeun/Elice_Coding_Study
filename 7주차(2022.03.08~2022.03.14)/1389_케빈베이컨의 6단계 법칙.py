from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]


for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs(start):
    bacon = [0] * (N + 1)
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                bacon[i] = bacon[v] + 1
                visited[i] = True
                queue.append(i)
    return sum(bacon)


result = []

for i in range(1, N + 1):
    visited = [False] * (N + 1)
    result.append(bfs(i))

print(result.index(min(result)) + 1)
