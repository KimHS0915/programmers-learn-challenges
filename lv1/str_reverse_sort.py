# 문자열 내림차순으로 배치하기

def solution(s):
    answer = ''
    lst = sorted(s, reverse=True)
    for i in lst:
        answer += i
    return answer