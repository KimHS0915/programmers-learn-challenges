# 2 x n 타일링

def solution(n):
    l, r = 1, 2
    for _ in range(n - 1):
        l, r = r, l + r
    return l % 1000000007
