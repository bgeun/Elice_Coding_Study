import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
ground = [list(map(int, input().split())) for i in range(n)]
result = []
max_g = max(map(max, ground))

for x in range(max_g, -1, -1):
    pop_inv = 0
    store_inv = 0
    time = 0
    for i in range(n):
        for j in range(m):
            if ground[i][j] < x:
                pop_inv += x - ground[i][j]

            else:
                store_inv += ground[i][j] - x

    inven = store_inv + b

    if inven < pop_inv:
        continue

    time = (2 * store_inv) + pop_inv
    result.append((time, x))

result.sort(key=lambda x: (x[0], -x[1]))
print(result[0][0], result[0][1])
