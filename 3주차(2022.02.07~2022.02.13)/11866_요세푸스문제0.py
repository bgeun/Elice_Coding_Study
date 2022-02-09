from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
queue = deque()
res = []

for i in range(1, n+1):
    queue.append(i)

while queue:
    for i in range(k-1):
        queue.append(queue.popleft())
    res.append(queue.popleft())

print('<', end="")
for i in res:
    print(i, end="")
    if i != res[-1]:
        print(",", end=" ")
print('>')
