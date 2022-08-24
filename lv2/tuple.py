# 튜플

def solution(s):
    lst = s[2:-2].split("},{")
    lst = sorted([set(i.split(",")) for i in lst], key=lambda x: len(x))
    answer = []
    for i in lst:
        answer.append(list(i.difference(set(answer)))[0])
    answer = [int(i) for i in answer]
    return answer
