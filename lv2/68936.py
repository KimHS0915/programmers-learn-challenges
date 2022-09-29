# 쿼드압축 후 개수 세기

def quad_comp(arr):
    n = len(arr)
    total = sum([sum(row) for row in arr])
    if total == 0:
        return [0]
    elif total == n * n:
        return [1]
    else:
        n = n // 2
        q1 = [v[:n] for i, v in enumerate(arr) if i < n]
        q2 = [v[:n] for i, v in enumerate(arr) if i >= n]
        q3 = [v[n:] for i, v in enumerate(arr) if i < n]
        q4 = [v[n:] for i, v in enumerate(arr) if i >= n]
        return quad_comp(q1) + quad_comp(q2) + quad_comp(q3) + quad_comp(q4)


def solution(arr):
    result = quad_comp(arr)
    cnt1 = sum(result)
    cnt0 = len(result) - cnt1
    return cnt0, cnt1
