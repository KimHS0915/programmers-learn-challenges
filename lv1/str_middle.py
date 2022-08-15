# 가운데 글자 가져오기

def solution(s):
    num = len(s) // 2
    if len(s) % 2 == 0:
        answer = s[num-1] + s[num]
    else:
        answer = s[num]
    return answer