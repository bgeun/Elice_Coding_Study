n = int(input())

cnt = 1
zip = 1

while(1):
    if zip>=n:
        break    
    zip += 6 * cnt
    cnt +=1

print(cnt)
