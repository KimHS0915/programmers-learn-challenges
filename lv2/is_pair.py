# 올바른 괄호

def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0:
                return False
            if stack.pop() != "(":
                return False
    return len(stack) == 0
