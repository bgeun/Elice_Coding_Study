def solution(numbers, hand):
    answer = ""

    dic = {
        1: [0, 0],
        2: [0, 1],
        3: [0, 2],
        4: [1, 0],
        5: [1, 1],
        6: [1, 2],
        7: [2, 0],
        8: [2, 1],
        9: [2, 2],
        "*": [3, 0],
        0: [3, 1],
        "#": [3, 2],
    }

    l_start = dic["*"]
    r_start = dic["#"]

    for i in numbers:
        cur = dic[i]
        if i in [1, 4, 7]:
            answer += "L"
            l_start = cur

        elif i in [3, 6, 9]:
            answer += "R"
            r_start = cur

        else:
            l_dis = abs(l_start[0] - cur[0]) + abs(l_start[1] - cur[1])
            r_dis = abs(r_start[0] - cur[0]) + abs(r_start[1] - cur[1])

            if l_dis < r_dis:
                answer += "L"
                l_start = cur
            elif l_dis > r_dis:
                answer += "R"
                r_start = cur
            else:
                if hand == "left":
                    answer += "L"
                    l_start = cur
                else:
                    answer += "R"
                    r_start = cur

    return answer
