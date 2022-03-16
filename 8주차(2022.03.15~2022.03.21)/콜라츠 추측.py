def solution(num):
    cnt = 0
    answer = 0
    while 1:
        if cnt >= 500:
            return -1
        if num == 1:
            return cnt
        if num % 2 == 0:
            num = num / 2
            cnt += 1
        else:
            num = (num * 3) + 1
            cnt += 1
