result = []

while(1):
    a, b, c = map(int, input().split())
    if(a == 0 and b == 0 and c == 0):
        break
    
    pow_a = pow(a,2)
    pow_b = pow(b,2)
    pow_c = pow(c,2)
    
    if(pow_a + pow_b == pow_c):
        result.append("right")
    elif(pow_b + pow_c == pow_a):
        result.append("right")
    elif(pow_c + pow_a == pow_b):
        result.append("right")
    else:
        result.append("wrong")

for i in range(len(result)):
    print(result[i])