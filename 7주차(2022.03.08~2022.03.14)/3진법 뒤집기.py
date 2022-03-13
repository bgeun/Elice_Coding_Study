def solution(n):
    answer = 0
    ternary = ""
    mul = 1
    while n >= 1:
        mod = n % 3
        n = n // 3
        ternary += str(mod)
    ternary = list(ternary)
    ternary.reverse()

    for i in ternary:
        answer += mul * int(i)
        mul *= 3

    return answer
