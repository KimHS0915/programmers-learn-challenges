# 나머지가 1이 되는 수 찾기

def solution(n):
    val = n
    for x in range(n, 0, -1):
        if n % x == 1 and x < val:
            val = x
    return val
    