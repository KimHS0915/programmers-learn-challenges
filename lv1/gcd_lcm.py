# 최대공약수와 최소공배수

def euclidean(n, m):
    tmp = m % n
    if tmp == 0:
        return n
    else:
        return euclidean(tmp, n)
    
def solution(n, m):
    gcd = euclidean(n, m)
    lcm = n*m // gcd
    return [gcd, lcm]