def solution(s):
    answer = ""
    L = s.split(" ")
    # L2 = s.split()
    # print(L)
    # print(L2)
    for i in L:
        i = i.capitalize()
        answer += i + " "

    # print(answer)
    return answer[:-1]
