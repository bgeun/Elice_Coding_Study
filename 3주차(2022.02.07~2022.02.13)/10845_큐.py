import sys
input = sys.stdin.readline

n = int(input())
queue = []

for _ in range(n):
    command = input().split()

    if len(command) == 2:
        queue.append(command[1])

    else:
        if command[0] == 'pop':
            try:
                print(queue.pop(0))
            except:
                print(-1)

        elif command[0] == 'size':
            print(len(queue))

        elif command[0] == 'empty':
            if not queue:
                print(1)
            else:
                print(0)

        elif command[0] == 'front':
            try:
                print(queue[0])
            except:
                print(-1)

        elif command[0] == 'back':
            try:
                print(queue[-1])
            except:
                print(-1)
