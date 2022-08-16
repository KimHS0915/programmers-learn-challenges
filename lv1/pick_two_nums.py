# 두 개 뽑아서 더하기

def solution(numbers):
    answer = []
    num_len = len(numbers)
    i = 0
    j = num_len - 1
    while i < num_len - 2:
        if j == 0 or j == i:
            j = num_len - 1
            i += 1
        answer.append(numbers[i] + numbers[j])
        if j > i:
            j -= 1         
    answer = set(answer)
    return sorted(answer)