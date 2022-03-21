def solution(sizes):
    answer = 0
    l = len(sizes)
    width = []
    height = []

    for i in range(l):
        sizes[i].sort()
        width.append(sizes[i][1])
        height.append(sizes[i][0])

    answer = max(width) * max(height)
    return answer
