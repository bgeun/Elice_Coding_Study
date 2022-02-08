import sys
input = sys.stdin.readline

while(1):
    string = input().rstrip()
    stack = []

    if string == ".":
        break

    for c in string:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
        elif c == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
    if len(stack) == 0:
        print('yes')
    else:
        print('no')
