# 실패율

def solution(N, stages):
    dic = {}
    for i in range(1, N+1):
        challenger = []
        failure = []
        for stage in stages:
            if stage == i:
                failure.append(stage)
            if stage >= i:
                challenger.append(stage)
        if not challenger:
            dic[i] = 0
        else:
            dic[i] = len(failure) / len(challenger)
    result = sorted(dic.items(), key=lambda item: item[1], reverse=True)
    return [i[0] for i in result]