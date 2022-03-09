import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

print(graph)


def bfs(start):
    num = [0] * (N + 1)

    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                num[i] = num[v] + 1
                queue.append(i)
                visited[i] = True
    print("num: ", num)
    return sum(num)


result = []

for i in range(1, N + 1):
    visited = [False] * (N + 1)
    result.append(bfs(i))
print("result: ", result)
print(result.index(min(result)) + 1)
