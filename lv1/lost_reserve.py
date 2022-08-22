# 체육복

def solution(n, lost, reserve):
    lst = [1] * (n + 2)
    for i in reserve:
        lst[i] += 1
    for i in lost:
        lst[i] -= 1
    for i in range(1, n + 1):
        if lst[i - 1] == 0 and lst[i] == 2:
            lst[i - 1], lst[i] = 1, 1
        elif lst[i] == 2 and lst[i + 1] == 0:
            lst[i], lst[i + 1] = 1, 1
    return sum([1 for i in lst[1:-1] if i])
