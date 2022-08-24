# 기능 개발

def solution(progresses, speeds):
    answer = []
    while len(progresses) > 0:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        cnt = 0
        while len(progresses) > 0 and progresses[0] >= 100:
            cnt += 1
            progresses = progresses[1:]
            speeds = speeds[1:]
        if cnt > 0:
            answer.append(cnt)
    return answer
