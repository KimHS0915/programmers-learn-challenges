# N개의 최소공배수

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    return (x * y) // gcd(x, y)


def solution(arr):
    while len(arr) >= 2:
        x = arr.pop()
        y = arr.pop()
        arr.append(lcm(x, y))
    return arr[0]
