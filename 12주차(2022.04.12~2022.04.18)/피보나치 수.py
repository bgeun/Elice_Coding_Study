def fib(n):
    cur, _next = 0, 1
    for _ in range(n):
        cur, _next = _next, cur + _next
    return cur


def solution(n):
    return fib(n) % 1234567
