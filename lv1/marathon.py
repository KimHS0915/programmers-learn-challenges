# 완주하지 못한 선수

def solution(participant, completion):
    answer = ''
    dic = {}
    for p in participant:
        if dic.get(p):
            dic[p] += 1
        else:
            dic[p] = 1
    for c in completion:
        dic[c] -= 1
    answer = [k for k, v in dic.items() if v > 0][0]
    return answer
