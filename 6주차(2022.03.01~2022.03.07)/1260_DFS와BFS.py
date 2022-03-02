from collections import deque
import sys

input = sys.stdin.readline

n, m, v = map(int, input().split())

array = [[] for _ in range(n + 1)]
result_dfs = 0
result_bfs = 0
visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)

for i in range(m):
    x, y = map(int, input().split())
    array[x].append(y)
    array[y].append(x)

for i in range(len(array)):
    array[i].sort()


def dfs(array, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in array[v]:
        if not visited[i]:
            dfs(array, i, visited)


def bfs(array, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in array[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(array, v, visited_dfs)
print()
bfs(array, v, visited_bfs)
