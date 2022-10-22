import heapq


def solution(alp, cop, problems):
    max_alp, max_cop = 0, 0
    problems.extend([[0, 0, 1, 0, 1], [0, 0, 0, 1, 1]])
    for problem in problems:
        max_alp, max_cop = max(max_alp, problem[0]), max(max_cop, problem[1])
    alp, cop = min(alp, max_alp), min(cop, max_cop)
    history = set()
    q = []
    heapq.heappush(q, (0, alp, cop))
    while True:
        curr = heapq.heappop(q)
        if curr in history:
            continue
        else:
            history.add(curr)
        if curr[1] >= max_alp and curr[2] >= max_cop:
            break
        for problem in problems:
            if curr[1] >= problem[0] and curr[2] >= problem[1]:
                heapq.heappush(q, (
                    curr[0] + problem[4],
                    min(curr[1] + problem[2], max_alp),
                    min(curr[2] + problem[3], max_cop),
                ))
    return curr[0]
