def getDivisor(num):
    cnt = 0
    i = 1
    while i * i <= num:
        if num % i == 0:
            if i * i == num:
                cnt += 1
                i += 1
                continue
            cnt += 2
        i += 1
    if cnt % 2 == 0:
        return True
    else:
        return False


def solution(left, right):
    answer = 0

    for i in range(left, right + 1):
        if getDivisor(i):
            answer += i
        else:
            answer -= i

    return answer
