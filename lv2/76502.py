# 괄호 회전하기

def is_valid_bracket(s):
    stack = []
    pair = {"]": "[", ")": "(", "}": "{"}
    s = list(s)
    for c in s:
        if c in pair:
            if len(stack) == 0:
                return False
            else:
                if stack.pop() != pair[c]:
                    return False
        else:
            stack.append(c)
    return len(stack) == 0


def solution(s):
    answer = 0
    slen = len(s)
    if slen % 2 != 0:
        return answer
    for i in range(slen):
        if is_valid_bracket(s):
            answer += 1
        s = s[1:] + s[:1]
    return answer
