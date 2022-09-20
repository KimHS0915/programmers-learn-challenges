# k진수에서 소수 개수 구하기

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def decimal_to_basek(n, k):
    ret = ""
    while n:
        n, r = divmod(n, k)
        ret += str(r)
    return ret[::-1]


def solution(n, k):
    nk = decimal_to_basek(n, k)
    lst = nk.split("0")
    answer = 0
    for i in lst:
        if i != "" and is_prime(int(i)):
            answer += 1
    return answer
