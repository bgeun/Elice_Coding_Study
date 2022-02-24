import heapq
import sys

input = sys.stdin.readline

N = int(input())
max_heap = []

for i in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(max_heap, (-x, x))
    else:
        try:
            print(heapq.heappop(max_heap)[1])
        except:
            print(0)
