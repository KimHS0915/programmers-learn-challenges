# 문자열 내 p와 y의 개수

def solution(s):
    answer = True
    if s.lower().count('p') != s.lower().count('y'):
        answer = False
    return answer
