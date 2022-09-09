# 점프와 순간 이동

def solution(n):
    k = 0
    while n > 0:
        if n % 2 == 0:
            n /= 2
        else:
            n -= 1
            k += 1
    return k
