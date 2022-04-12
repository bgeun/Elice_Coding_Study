def solution(s):
    answer = ""
    lst = list(map(int, s.split()))

    lst.sort()
    answer += str(lst[0])

    lst.sort(reverse=True)
    answer += " " + str(lst[0])

    return answer
