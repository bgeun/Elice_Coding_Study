import math


def solution(progresses, speeds):
    answer = []
    arr = []
    late = 0

    for p, s in zip(progresses, speeds):
        arr.append(math.ceil((100 - p) / s))

    for i in range(len(arr)):
        if arr[i] > arr[late]:
            answer.append(i - late)
            late = i
    answer.append(len(arr) - late)
    print(arr)
    return answer
