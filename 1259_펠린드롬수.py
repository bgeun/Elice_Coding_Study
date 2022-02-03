from audioop import reverse


result = []

while(1):
    n = input()
    if n == '0':
        break
    
    reverse_n = n[::-1]
    if(n == reverse_n):
        result.append('yes')
    else:
        result.append('no')

for i in result:
    print(i)