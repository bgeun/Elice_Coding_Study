n = int(input())

for i in range(1,n+1):
    constructor = sum(map(int, str(i)))
    
    num = i + constructor
    
    if num == n:
        print(i)
        break
    
    if n == i:
        print(0)
        break