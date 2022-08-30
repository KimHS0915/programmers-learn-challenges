# 줄 서는 방법

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def solution(n, k):
    answer = []
    nums = list(range(1, n + 1))
    while n > 0:
        idx, k = divmod(k, factorial(n) // n)
        if k == 0:
            idx -= 1
        answer.append(nums.pop(idx))
        n -= 1
    return answer
