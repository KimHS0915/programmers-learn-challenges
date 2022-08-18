# 124 나라의 숫자

def solution(n):
    code = "124"
    answer = ""
    while n > 0:
        n -= 1
        n, mod = divmod(n, 3)
        answer += code[mod]
    return answer[::-1]
