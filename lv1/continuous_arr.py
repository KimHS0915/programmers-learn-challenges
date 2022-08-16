# 같은 숫자는 싫어

def solution(arr):
    answer = []
    i = 0
    while True:
        if arr[i] != arr[i+1]:
            answer.append(arr[i])
        i += 1
        if i + 1 == len(arr):
            answer.append(arr[i])
            return answer