# 프린터

def solution(priorities, location):
    lst = []
    for i, v in enumerate(priorities):
        lst.append([i, v])
    answer = []
    while True:
        pair = lst.pop(0)
        if len(lst) < 1:
            answer.append(pair)
            break
        if pair[1] < max(lst, key=lambda x: x[1])[1]:
            lst.append(pair)
        else:
            answer.append(pair)
    return answer.index([location, priorities[location]]) + 1
