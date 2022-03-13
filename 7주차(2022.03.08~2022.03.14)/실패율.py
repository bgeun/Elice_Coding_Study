def solution(N, stages):
    answer = []
    length = len(stages)
    result = []
    dic = {}

    for i in range(1, N + 1):
        clear = stages.count(i)
        if length == 0:
            dic[i] = 0
            continue
        dic[i] = clear / length
        length -= clear

    answer = sorted(dic, key=lambda x: -dic[x])

    return answer
