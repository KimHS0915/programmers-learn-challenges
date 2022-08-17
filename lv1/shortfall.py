# 부족한 금액 계산하기

def solution(price, money, count):
    total = sum([price * i for i in range(1, count + 1)])
    result = total - money
    return 0 if result < 0 else result
