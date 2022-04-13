def solution(arr):
    m = max(arr)
    while True:
        cnt = 0
        for i in arr:
            if m % i == 0:
                cnt += 1
            else:
                break
        if cnt == len(arr):
            return m
        m += 1
