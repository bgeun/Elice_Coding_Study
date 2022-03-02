import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for i in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


dfs(graph, 1, visited)

res = list(filter(lambda x: x == True, visited))
print(len(res) - 1)
