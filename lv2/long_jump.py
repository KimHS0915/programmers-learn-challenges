# 멀리뛰기

def solution(n):
    l, r = 1, 1
    for _ in range(n - 1):
        l, r = r, l + r
    return r % 1234567
