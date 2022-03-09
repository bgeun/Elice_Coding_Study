import sys

input = sys.stdin.readline

N = int(input())
room = []
cnt = 1

for i in range(N):
    x, y = map(int, input().split())
    room.append((x, y))

room.sort(key=lambda x: (x[1], x[0]))
end = room[0][1]

for i in range(1, N):
    if end <= room[i][0]:
        cnt += 1
        end = room[i][1]

print(cnt)
