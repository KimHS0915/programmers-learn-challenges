# 제일 작은 수 제거하기

def solution(arr):
    x = arr[:]
    x.sort()
    arr.remove(x[0])
    return arr if len(arr) != 0 else [-1]