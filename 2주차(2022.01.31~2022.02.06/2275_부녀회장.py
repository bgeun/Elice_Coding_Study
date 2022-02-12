apt = [[0 for j in range(14)] for i in range(15)]

# 각 층의 1호 초기화
for i in range(15):
    apt[i][0] = 1
# 0층의 호 초기화 
for i in range(14):
    apt[0][i] = i + 1

for i in range(1,15):
    for j in range(1,14):
        apt[i][j] = apt[i][j-1] + apt[i-1][j]

result = []

t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    result.append(apt[k][n-1])

for i in range(t):
    print(result[i])