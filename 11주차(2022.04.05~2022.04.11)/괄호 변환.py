# p를 u, v로 분리
def sepUV(p):
    left = 0
    right = 0
    for i in range(len(p)):
        if p[i] == "(":
            left += 1
        elif p[i] == ")":
            right += 1
        if left == right:
            return p[: i + 1], p[i + 1 :]


# u가 올바른 괄호인지 확인
def check(u):
    stack = []
    for c in u:
        if c == "(":
            stack.append(c)
        else:
            if not len(stack):
                return False
            elif stack[-1] == "(":
                stack.pop()
    if len(stack):
        return False
    else:
        return True


def solution(p):
    answer = ""
    # 과정 1
    if not p:
        return ""
    # 과정 2
    u, v = sepUV(p)

    # 과정 3
    if check(u):
        # 과정 3-1
        return u + solution(v)

    # 과정 4-1
    answer += "("
    # 과정 4-2
    answer += solution(v)
    # 과정 4-3
    answer += ")"

    u = u[1:-1]
    # 과정 4-4
    for c in u:
        if c == "(":
            answer += ")"
        else:
            answer += "("

    return answer
