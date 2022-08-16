# 정수 내림차순으로 배치하기

def solution(n):
    lst = sorted(str(n), reverse=True)
    answer = ''
    for i in lst:
        answer += i
    return int(answer)