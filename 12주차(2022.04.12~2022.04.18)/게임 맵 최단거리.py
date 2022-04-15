from collections import deque


def solution(maps):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    mx = len(maps)
    my = len(maps[0])

    visited = [[False for _ in range(my)] for _ in range(mx)]
    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= mx or ny < 0 or ny >= my:
                continue
            if visited[nx][ny] == False and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                visited[nx][ny] = True
                queue.append((nx, ny))

    if maps[mx - 1][my - 1] == 1:
        return -1
    return maps[mx - 1][my - 1]
