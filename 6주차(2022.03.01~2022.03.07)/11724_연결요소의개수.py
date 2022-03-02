import sys

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


def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


for i in range(1, len(visited)):
    if visited[i] == False:
        cnt += 1
        dfs(graph, i, visited)

print(cnt)
