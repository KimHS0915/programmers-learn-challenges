# 이상한 문자 만들기

def solution(s):
    answer = ''
    word_idx = 0
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
            word_idx = 0
        elif word_idx % 2 == 0:
            answer += s[i].upper()
            word_idx += 1
        else:
            answer += s[i].lower()
            word_idx += 1
    return answer