# 자연수 뒤집어 배열로 만들기

def solution(n):
    return [int(num) for num in str(n)][::-1]