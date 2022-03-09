from collections import deque
import sys

input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in graph:
    i.sort()


def dfs(v):
    visited_dfs[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited_dfs[i]:
            dfs(i)


def bfs(v):
    queue = deque()
    queue.append(v)
    visited_bfs[v] = True
    while queue:
        x = queue.popleft()
        print(x, end=" ")
        for i in graph[x]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True


dfs(V)
print()
bfs(V)
