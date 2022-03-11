def solution(answers):
    answer = []
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    result = [0] * 4

    for i in range(len(answers)):
        if answers[i] == supo1[i % len(supo1)]:
            result[1] += 1
        if answers[i] == supo2[i % len(supo2)]:
            result[2] += 1
        if answers[i] == supo3[i % len(supo3)]:
            result[3] += 1

    maxR = max(result)
    for i in range(len(result)):
        if maxR == result[i]:
            answer.append(result.index(maxR))
            result[i] = 0

    return answer
