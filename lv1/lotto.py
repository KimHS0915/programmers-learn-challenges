# 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    cnt_unknown = 0
    cnt_correct = 0
    for i in lottos:
        if i == 0:
            cnt_unknown += 1
        elif i in win_nums:
            cnt_correct += 1
    rank = [6] + list(range(6, 0, -1))
    return [rank[cnt_correct + cnt_unknown], rank[cnt_correct]]
    