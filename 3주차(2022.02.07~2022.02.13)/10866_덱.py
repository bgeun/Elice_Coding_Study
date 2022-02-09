import sys
input = sys.stdin.readline

n = int(input())
deque = []

for _ in range(n):
    command = input().split()

    if len(command) == 2:

        if command[0] == 'push_front':
            deque.insert(0, command[1])

        elif command[0] == 'push_back':
            deque.append(command[1])

    else:
        if command[0] == 'pop_front':
            try:
                print(deque.pop(0))
            except:
                print(-1)

        elif command[0] == 'pop_back':
            try:
                print(deque.pop())
            except:
                print(-1)

        elif command[0] == 'size':
            print(len(deque))

        elif command[0] == 'empty':
            if not deque:
                print(1)
            else:
                print(0)

        elif command[0] == 'front':
            try:
                print(deque[0])
            except:
                print(-1)

        elif command[0] == 'back':
            try:
                print(deque[-1])
            except:
                print(-1)
