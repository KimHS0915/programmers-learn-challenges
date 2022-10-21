# 정수 삼각형

def solution(triangle):
    row = len(triangle) - 2
    while row >= 0:
        for col in range(len(triangle[row])):
            triangle[row][col] = triangle[row][col] + \
                max(triangle[row + 1][col], triangle[row + 1][col + 1])
        row -= 1
    return triangle[0][0]
