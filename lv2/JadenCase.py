# JadenCase 문자열 만들기

def solution(s):
    answer = ''
    first_c = True
    for c in s:
        if c == " ":
            first_c = True
        elif first_c:
            first_c = False
            c = c.upper()
        else:
            c = c.lower()
        answer += c
    return answer
