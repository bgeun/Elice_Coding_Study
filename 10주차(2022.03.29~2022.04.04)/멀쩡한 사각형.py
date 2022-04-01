import math


def solution(w, h):
    answer = 0
    gcd = math.gcd(w, h)
    total = w * h
    answer = total - (w + h - gcd)
    return answer
