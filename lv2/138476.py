# 귤 고르기

def solution(k, tangerine):
    answer = 0
    dic = {}
    for t in tangerine:
        if dic.get(t):
            dic[t] += 1
        else:
            dic[t] = 1
    lst = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    for l in lst:
        k -= l[1]
        answer += 1
        if k <= 0:
            break
    return answer
