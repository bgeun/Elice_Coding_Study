def solution(s):
    answer = []
    if len(s) == 1:
        return 1
    for i in range(1, len(s) // 2 + 1):
        res = ""
        cnt = 1
        tmp = s[:i]

        for j in range(i, len(s) + i, i):
            if tmp == s[j : i + j]:
                cnt += 1
            else:
                if cnt == 1:
                    res += tmp
                else:
                    res = res + str(cnt) + tmp
                tmp = s[j : i + j]
                cnt = 1
        answer.append(len(res))

    return min(answer)
