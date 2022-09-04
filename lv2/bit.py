# 2개 이하로 다른 비트

def solution(numbers):
    answer = []
    for n in numbers:
        if n % 2 == 0:
            answer.append(n + 1)
        else:
            b = '0' + format(n, 'b')
            idx = b.rfind('0')
            b = b[:idx] + '1' + '0' + b[idx + 2:]
            answer.append(int(b, 2))
    return answer
