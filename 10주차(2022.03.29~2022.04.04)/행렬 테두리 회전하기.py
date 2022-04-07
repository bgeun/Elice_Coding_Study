def solution(rows, columns, queries):
    answer = []
    box = [[0 for _ in range(columns + 1)] for _ in range(rows + 1)]
    cnt = 1

    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            box[i][j] = cnt
            cnt += 1

    for x1, y1, x2, y2 in queries:
        tmp = box[x1][y1]
        min_num = tmp

        for i in range(x1, x2):
            new = box[i + 1][y1]
            box[i][y1] = new
            min_num = min(min_num, new)

        for i in range(y1, y2):
            new = box[x2][i + 1]
            box[x2][i] = new
            min_num = min(min_num, new)

        for i in range(x2, x1, -1):
            new = box[i - 1][y2]
            box[i][y2] = new
            min_num = min(min_num, new)

        for i in range(y2, y1, -1):
            new = box[x1][i - 1]
            box[x1][i] = new
            min_num = min(min_num, new)

        box[x1][y1 + 1] = tmp
        answer.append(min_num)

    return answer
