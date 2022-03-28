def solution(dartResult):
    stack = []
    dartResult = dartResult.replace("10", "a")
    score = {"S": 1, "D": 2, "T": 3}

    for i in dartResult:
        if i.isdigit() or i == "a":
            stack.append(10 if i == "a" else int(i))
        elif i in ("S", "D", "T"):
            num = stack.pop()
            stack.append(num ** score[i])
        elif i == "#":
            stack[-1] = stack[-1] * -1
        elif i == "*":
            num = stack.pop()
            if len(stack):
                stack[-1] = stack[-1] * 2
            stack.append(num * 2)
    return sum(stack)
