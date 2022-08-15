# 두 정수 사이의 합

def solution(a, b):
    if a > b :
        start_num, end_num = b, a + 1
    else:
        start_num, end_num = a, b + 1
    answer = 0   
    for i in range(start_num, end_num):
        answer += i
    return answer