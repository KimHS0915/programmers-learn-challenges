# 모의고사

def solution(answers):
    return_answer = []
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == p1[i%len(p1)]:
            scores[0] += 1
        if answers[i] == p2[i%len(p2)]:
            scores[1] += 1
        if answers[i] == p3[i%len(p3)]:
            scores[2] += 1
    for idx, score in enumerate(scores):
        if score == max(scores):
            return_answer.append(idx + 1)           
    return return_answer