def solution(n):
    answer = ""

    while n:
        if n % 3 == 0:
            answer += "4"
            n = (n // 3) - 1
        else:
            answer += str(n % 3)
            n = n // 3

    answer = answer[::-1]

    return answer
