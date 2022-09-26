# 삼각 달팽이

def solution(n):
    answer = [[0 for _ in range(i + 1)] for i in range(n)]
    row, col = -1, 0
    num = 1
    for i in range(n):
        for _ in range(i, n):
            if i % 3 == 0:
                row += 1
            elif i % 3 == 1:
                col += 1
            else:
                row, col = row - 1, col - 1
            answer[row][col] = num
            num += 1
    return sum(answer, [])
