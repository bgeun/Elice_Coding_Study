def solution(s):
    stack = []
    
    for i in s:
        try:  
            if stack[-1] == i:
                stack.pop()
            else: stack.append(i)
        except:
            stack.append(i)
            
    if len(stack) == 0:
        return 1
    else:
        return 0