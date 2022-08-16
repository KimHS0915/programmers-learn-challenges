# 완주하지 못한 선수

import collections

def solution(participant, completion):
    x =  collections.Counter(participant) - collections.Counter(completion)
    return list(x)[0]