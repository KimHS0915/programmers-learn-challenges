# 이진 변환 반복하기

def solution(s):
    answer = [0, 0]
    while s != "1":
        cnt_1 = s.count("1")
        answer[1] += len(s) - cnt_1
        s = format(cnt_1, "b")
        answer[0] += 1
    return answer
