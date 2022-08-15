# 소수 찾기

def solution(n):
    sieve = [False, False] + [True]*(n-1)
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            sieve[i+i::i] = [False]*len(sieve[i+i::i])
    prime_list = [num for num, bol in enumerate(sieve) if bol]
    return len(prime_list)