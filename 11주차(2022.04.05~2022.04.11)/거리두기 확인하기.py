from collections import deque


def bfs(place):
    start = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                start.append([i, j])
    print(start)
    for s in start:
        queue = deque([s])
        visited = [[False] * 5 for _ in range(5)]
        dist = [[0] * 5 for _ in range(5)]
        visited[s[0]][s[1]] = True

        while queue:
            y, x = queue.popleft()

            dx = [-1, 1, 0, 0]  # 좌우
            dy = [0, 0, -1, 1]  # 상하

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < 5 and 0 <= ny < 5 and not visited[ny][nx]:

                    if place[ny][nx] == "O":
                        queue.append([ny, nx])
                        visited[ny][nx] = True
                        dist[ny][nx] = dist[y][x] + 1

                    if place[ny][nx] == "P" and dist[y][x] <= 1:
                        return 0
    return 1


def solution(places):
    answer = []
    for place in places:
        answer.append(bfs(place))
    return answer
