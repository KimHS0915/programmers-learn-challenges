# 피로도

from itertools import permutations


def solution(k, dungeons):
    size = len(dungeons)
    perms = permutations(dungeons, size)
    cnts = []
    for i in perms:
        fatigue = k
        cnt = 0
        for j in i:
            if fatigue < j[0]:
                break
            fatigue -= j[1]
            cnt += 1
            if cnt == size:
                return cnt
        cnts.append(cnt)
    return max(cnts)
