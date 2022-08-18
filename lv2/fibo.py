# 피보나치 수

def fibo(n):
    if n == 0:
        return 0
    left, right = 0, 1
    for _ in range(n - 1):
        left, right = right, left + right
    return right


def solution(n):
    return fibo(n) % 1234567
