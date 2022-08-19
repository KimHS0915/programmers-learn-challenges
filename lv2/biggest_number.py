# 가장 큰 수

def solution(numbers):
    answer = "".join(
        sorted([str(n) for n in numbers],
               key=lambda x: (x * 4)[:4], reverse=True)
    )
    return answer if answer[0] != "0" else "0"
