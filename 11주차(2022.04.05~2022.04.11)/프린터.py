from collections import deque


def solution(priorities, location):
    arr = []
    cnt = 0
    for i, v in enumerate(priorities):
        arr.append((i, v))
    print(arr)
    queue = deque(arr)

    while queue:
        flag = 0
        x = queue.popleft()
        for i in range(0, len(queue)):
            if x[1] < queue[i][1]:
                queue.append(x)
                flag = 1
                break
        # print(x)
        if flag == 0:
            cnt += 1
            if x[0] == location:
                return cnt
