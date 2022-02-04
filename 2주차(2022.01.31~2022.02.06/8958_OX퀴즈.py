n = int(input())

arr = []
result = [0] * n

for i in range(n):
    arr.append(list(input()));

for i in range(n):
    cnt = 0
    for j in range(len(arr[i])):
        if(arr[i][j] == 'O'):
            cnt += 1;
            result[i] += cnt;
        else:
            cnt = 0;

for i in result:
    print(i)
        
