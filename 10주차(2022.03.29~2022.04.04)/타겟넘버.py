from collections import deque


def solution(numbers, target):
    answer = 0
    idx = 0
    n = len(numbers)
    queue = deque()
    queue.append([numbers[0], 0])
    queue.append([-1 * numbers[0], 0])

    while queue:
        x, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append([x + numbers[idx], idx])
            queue.append([x - numbers[idx], idx])
        else:
            if x == target:
                answer += 1
    return answer
