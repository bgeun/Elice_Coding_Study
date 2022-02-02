result = []

t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())

    floor = n % h
    ho = n // h + 1

    if(ho < 10):
        result.append(str(floor) + "0" + str(ho))
    else:
        result.append(str(floor) + str(ho))

for i in range(t):
    print(result[i]) 

