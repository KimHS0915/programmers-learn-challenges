# 소수 만들기

from itertools import combinations

def get_sieve(n):
    sieve = [False, False] + [True] * (n - 1)
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i+i::i] = [False] * len(sieve[i+i::i])
    return sieve

def solution(nums):
    sieve = get_sieve(3000)
    combs = combinations(nums, 3)
    return sum([sieve[sum(i)] for i in combs])
