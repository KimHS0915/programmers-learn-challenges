# 타겟 넘버

def solution(numbers, target):
    lst = [0]
    for n in numbers:
        tmp = []
        for i in lst:
            tmp.append(i + n)
            tmp.append(i - n)
        lst = tmp
    return sum([1 for i in lst if i == target])
