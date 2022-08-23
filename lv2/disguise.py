# 위장

def solution(clothes):
    dic = {}
    for _, type in clothes:
        if dic.get(type):
            dic[type] += 1
        else:
            dic[type] = 1
    answer = 1
    for i in dic.values():
        answer *= i + 1
    answer -= 1
    return answer
