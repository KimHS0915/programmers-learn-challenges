# 문자열 다루기 기본

def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    try:
        int(s)
        return True
    except ValueError:
        return False