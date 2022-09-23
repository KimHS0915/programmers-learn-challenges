# 두 큐 합 같게 만들기

from collections import deque


def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)
    for i in range(len(queue1) * 4):
        if sum1 > sum2:
            sum1, sum2 = sum1 - q1[0], sum2 + q1[0]
            q2.append(q1.popleft())
        elif sum1 < sum2:
            sum1, sum2 = sum1 + q2[0], sum2 - q2[0]
            q1.append(q2.popleft())
        else:
            return i
    return -1
