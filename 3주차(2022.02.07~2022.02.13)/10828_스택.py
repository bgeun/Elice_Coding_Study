import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    command = input().split()
    if len(command) == 2:
        stack.append(command[1])

    else:
        if command[0] == 'pop':
            try:
                print(stack.pop())
            except:
                print(-1)

        elif command[0] == 'size':
            print(len(stack))

        elif command[0] == 'empty':
            if not stack:
                print(1)
            else:
                print(0)

        elif command[0] == 'top':
            try:
                print(stack[-1])
            except:
                print(-1)
