# 가장 먼 노드

from collections import deque


def solution(n, edge):
    dic = {}
    for node in edge:
        if dic.get(node[0]):
            dic[node[0]].append(node[1])
        else:
            dic[node[0]] = [node[1]]
        if dic.get(node[1]):
            dic[node[1]].append(node[0])
        else:
            dic[node[1]] = [node[0]]
    dist = [0, 1] + [0] * (n - 1)
    q = deque([1])
    while q:
        curr = q.popleft()
        for node in dic[curr]:
            if not dist[node]:
                q.append(node)
                dist[node] = dist[curr] + 1
    max_value = max(dist)
    return len([d for d in dist if d == max_value])
