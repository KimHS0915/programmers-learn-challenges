# 캐시

from collections import deque


def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    answer = 0
    caches = deque()
    for city in cities:
        city = city.lower()
        if city in caches:
            caches.remove(city)
            caches.append(city)
            answer += 1
        else:
            if len(caches) >= cacheSize:
                caches.popleft()
            caches.append(city)
            answer += 5
    return answer
