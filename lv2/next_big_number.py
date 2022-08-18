# 다음 큰 숫자

def dec2bin(n):
    bin = ""
    while n > 0:
        n, mod = divmod(n, 2)
        bin += str(mod)
    return bin[::-1]


def solution(n):
    n_cnt = dec2bin(n).count("1")
    for i in range(n + 1, 1000001):
        if n_cnt == dec2bin(i).count("1"):
            return i
    return None
