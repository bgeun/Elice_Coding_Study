import sys

input = sys.stdin.readline

n = int(input())
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]  # 북 서 남 동

for i in range(n):
    posX = 0
    posY = 0
    posDir = 0  # 0북 1서 2남 3동
    move = list(input())
    trace = [(posX, posY)]

    for j in move:
        if j == "F":
            posX = posX + dx[posDir]
            posY = posY + dy[posDir]
        elif j == "B":
            posX = posX - dx[posDir]
            posY = posY - dy[posDir]
        elif j == "L":
            if posDir == 3:
                posDir = 0
            else:
                posDir += 1
        elif j == "R":
            if posDir == 0:
                posDir = 3
            else:
                posDir -= 1
        trace.append((posX, posY))

    width = max(trace, key=lambda x: x[0])[0] - min(trace, key=lambda x: x[0])[0]
    height = max(trace, key=lambda x: x[1])[1] - min(trace, key=lambda x: x[1])[1]
    print(width * height)
