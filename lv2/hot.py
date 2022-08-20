# 더 맵게

import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        min1 = heapq.heappop(scoville)
        if min1 > K:
            break
        if len(scoville) == 0:
            return - 1
        min2 = heapq.heappop(scoville)
        mix = min1 + min2 * 2
        heapq.heappush(scoville, mix)
        answer += 1
    return answer
