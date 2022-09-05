# 소수 찾기

from itertools import permutations


def get_sieve(n):
    sieve = [False, False] + [True] * (n - 1)
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i+i::i] = [False] * len(sieve[i+i::i])
    return sieve


def solution(numbers):
    perms = []
    for i in range(1, len(numbers) + 1):
        perms += list(permutations(numbers, i))
    perms = [int("".join(i)) for i in perms]
    sieve = get_sieve(max(perms))
    primes = []
    for i in set(perms):
        if sieve[i]:
            primes.append(i)
    return len(primes)
