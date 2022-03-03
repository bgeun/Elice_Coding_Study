import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for i in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


# def dfs(graph, v, visited):
#     visited[v] = True
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)


# dfs(graph, 1, visited)

# res = list(filter(lambda x: x == True, visited))
# print(len(res) - 1)


def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


bfs(1)
res = list(filter(lambda x: x == True, visited))
print(len(res) - 1)
