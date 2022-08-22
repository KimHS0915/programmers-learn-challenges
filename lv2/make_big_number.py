# 큰수 만들기

def solution(number, k):
    answer = []
    for i in range(len(number)):
        while len(answer) > 0 and answer[-1] < number[i] and k > 0:
            answer.pop()
            k -= 1
        if k == 0:
            answer += list(number[i:])
            break
        answer.append(number[i])
    answer = answer[:-k] if k > 0 else answer
    return "".join(answer)
