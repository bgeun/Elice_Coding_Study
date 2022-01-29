t = int(input());

arr = []

for i in range(t):
    arr.append(list(input().split()))

for i in range(t):
    for j in range(len(arr[i][1])):
        print(arr[i][1][j] * int(arr[i][0]), end='')
        
    print()
