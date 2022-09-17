# 괄호 변환

def is_valid_bracket(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            else:
                if stack.pop() != "(":
                    return False
    return len(stack) == 0


def solution(p):
    if is_valid_bracket(p):
        return p
    dic = {"(": 0, ")": 0}
    for i in range(len(p)):
        dic[p[i]] += 1
        if dic["("] == dic[")"]:
            u, v = p[:i+1], p[i+1:]
            break
    if is_valid_bracket(u):
        return u + solution(v)
    else:
        new_u = ""
        for i in u[1:-1]:
            new_u += ")" if i == "(" else "("
        return "(" + solution(v) + ")" + new_u
