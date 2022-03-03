import sys
from collections import deque

sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
cnt = 0

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


# def dfs(graph, v, visited):
#     visited[v] = True
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)


# for i in range(1, len(visited)):
#     if visited[i] == False:
#         cnt += 1
#         dfs(graph, i, visited)

# print(cnt)


def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


cnt = 0

for i in range(1, N + 1):
    if visited[i] == False:
        cnt += 1
        bfs(i)

print(cnt)
