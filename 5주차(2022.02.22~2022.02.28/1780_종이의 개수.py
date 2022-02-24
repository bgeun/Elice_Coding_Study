import sys

input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

cnt = [0, 0, 0]  # -1, 0, 1


def cut(x, y, N):
    check = paper[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if check != paper[i][j]:  # 종이가 모두 같은 수 인지 검사
                cut(x, y, N // 3)
                cut(x, y + N // 3, N // 3)
                cut(x, y + (N // 3 * 2), N // 3)
                cut(x + N // 3, y, N // 3)
                cut(x + N // 3, y + N // 3, N // 3)
                cut(x + N // 3, y + (N // 3 * 2), N // 3)
                cut(x + N // 3 * 2, y, N // 3)
                cut(x + N // 3 * 2, y + N // 3, N // 3)
                cut(x + N // 3 * 2, y + N // 3 * 2, N // 3)
                return

    if check == -1:
        cnt[0] += 1
        return
    elif check == 0:
        cnt[1] += 1
        return
    else:
        cnt[2] += 1
        return


cut(0, 0, N)

for i in cnt:
    print(i)
