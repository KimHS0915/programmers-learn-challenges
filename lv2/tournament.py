# 예상 대진표

import math


def solution(n, a, b):
    answer = 1
    while abs(a - b) != 1 or (math.ceil(a / 2) != math.ceil(b / 2) and abs(a - b) == 1):
        a, b = math.ceil(a / 2), math.ceil(b / 2)
        answer += 1
    return answer
