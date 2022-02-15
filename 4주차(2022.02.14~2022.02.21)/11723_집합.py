import sys
input = sys.stdin.readline

arr = []

m = int(input())

for i in range(m):
    cal = input().split()
    if len(cal) == 2:
        cal[1] = int(cal[1])

    if(cal[0] == "add"):
        if cal[1] in arr:
            continue
        else:
            arr.append(cal[1])

    if(cal[0] == "remove"):
        if cal[1] not in arr:
            continue
        else:
            try:
                arr.remove(cal[1])
            except:
                continue

    if(cal[0] == "check"):
        if cal[1] in arr:
            print(1)
        else:
            print(0)

    if(cal[0] == "toggle"):
        if cal[1] in arr:
            arr.remove(cal[1])
        else:
            arr.append(cal[1])

    if(cal[0] == "all"):
        arr = [i for i in range(1, 21)]

    if(cal[0] == "empty"):
        arr = []
