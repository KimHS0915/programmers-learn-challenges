# 모음사전

from itertools import product


def solution(word):
    words = []
    for i in range(5):
        words.extend(["".join(j) for j in product("AEIOU", repeat=i + 1)])
    return sorted(words).index(word) + 1
