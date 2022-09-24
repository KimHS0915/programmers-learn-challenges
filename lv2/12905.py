# 가장 큰 정사각형 찾기

def solution(board):
    answer = 0
    row, col = len(board), len(board[0])
    for i in range(1, row):
        for j in range(1, col):
            if board[i][j] == 1:
                board[i][j] = 1 + min(board[i - 1][j - 1],
                                      board[i - 1][j],
                                      board[i][j - 1])
                answer = max(answer, board[i][j])
    return answer ** 2
