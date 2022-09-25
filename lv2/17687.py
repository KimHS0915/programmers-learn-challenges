# n진수  게임

def convert(n, base):
    if n == 0:
        return "0"
    tmp = "0123456789ABCDEF"
    ret = ""
    while n:
        n, r = divmod(n, base)
        ret += tmp[r]
    return ret[::-1]


def solution(n, t, m, p):
    answer = ""
    tmp = ""
    for i in range(t * m):
        tmp += convert(i, n)
    for i in range(p - 1, t * m, m):
        answer += tmp[i]
    return answer
