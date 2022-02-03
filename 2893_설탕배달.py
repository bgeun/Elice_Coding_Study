n = int(input())

wrap = 0

while(1):
    if n < 0:
        print(-1)
        break
    if n % 5 == 0:
        wrap += n // 5
        print(wrap)
        break
    n -= 3
    wrap += 1