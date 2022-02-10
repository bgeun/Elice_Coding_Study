from collections import deque
from os import rename
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    prop = deque(map(int, input().split()))
    queue = deque(range(n))
    cnt = 0

    while queue:
        if prop[queue[0]] == max(prop):
            if queue[0] == m:
                print(cnt + 1)
                break

            prop[queue[0]] = 0
            queue.popleft()
            cnt += 1

        else:
            queue.append(queue.popleft())
