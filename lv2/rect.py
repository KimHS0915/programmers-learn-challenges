# 멀쩡한 사각형

def gcd(x, y):
    if y % x == 0:
        return x
    return gcd(y % x, x)


def solution(w, h):
    return w * h - (w + h - gcd(w, h))
