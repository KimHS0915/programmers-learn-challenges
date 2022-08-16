# 시저 암호

def solution(s, n):
    string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer = ''
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
        else:            
            string_idx = string.index(s[i].upper())
            idx = (string_idx + n) % len(string)
            answer += string[idx] if s[i].isupper() else string[idx].lower()
    return answer