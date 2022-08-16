# 약수의 개수와 덧셈

def count_devide(n):
    cnt = 0
    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1
    return cnt

def solution(left, right):
    answer = 0
    if left >= right:
        return
    for i in range(left, right + 1):
        result = count_devide(i)
        if result % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer