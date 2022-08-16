# 체육복

def solution(n, lost, reserve):
    lst = [1] * n
    for l in lost:
        lst[l-1] = 0
    reserve2 = []
    reserve.sort()
    for r in reserve:
        if lst[r-1] == 0:
            lst[r-1] = 1
        elif r == 1 or lst[r-2] != 0:
            reserve2.append(r)
        elif lst[r-2] == 0:
            lst[r-2] = 1
    for r2 in reserve2:
        if r2 == n:
            pass
        elif lst[r2] == 0:
            lst[r2] = 1
    return lst.count(1)