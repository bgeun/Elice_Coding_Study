n, m = map(int, input().split())

arr = [list(str(input())) for _ in range(n)]
paint = []


def check(i, j):  # 잘라온 체스판에서 칠해야하는 정사각형의 수를 구하는 함수
    w_cnt = 0  # W로 시작했을 때 칠해야하는 수
    b_cnt = 0  # B로 시작했을 때 칠해야하는 수

    for x in range(i, i+8):
        for y in range(j, j+8):
            if (x + y) % 2 == 0:
                if arr[x][y] != "B":
                    b_cnt += 1  # B로 시작했는데 짝수 칸이 B가 아닐경우
                if arr[x][y] != "W":
                    w_cnt += 1
            else:
                if arr[x][y] != "W":  # B로 시작했는데 홀수 칸이 W가 아닐경우
                    b_cnt += 1
                if arr[x][y] != "B":
                    w_cnt += 1
    paint.append(b_cnt)
    paint.append(w_cnt)


# 자를 체스판 위치 변경
for i in range(n-7):
    for j in range(m-7):
        check(i, j)

print(paint)
print(min(paint))
