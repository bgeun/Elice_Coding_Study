import sys

input = sys.stdin.readline

n = int(input())

mRoom = [list(map(int, input().split())) for _ in range(n)]

mRoom.sort(key=lambda x: (x[1], x[0]))

end = mRoom[0][1]
use = 1
for i in range(1, n):
    if end <= mRoom[i][0]:
        end = mRoom[i][1]
        use += 1


print(use)
