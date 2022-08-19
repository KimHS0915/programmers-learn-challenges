# 카펫

def solution(brown, yellow):
    total = brown + yellow
    for w in range(total // 2, 1, -1):
        if total % w == 0:
            h = total / w
            if (w - 2) * (h - 2) == yellow:
                return [w, h]
    return []
