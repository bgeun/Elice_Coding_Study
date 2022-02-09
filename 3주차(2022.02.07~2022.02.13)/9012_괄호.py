import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    vps = input().rstrip()
    stack = []

    for c in vps:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break

    if len(stack) == 0:
        print('YES')
    else:
        print('NO')
