# 크레인 인형뽑기 게임

def solution(board, moves):
    board_stack = [[] for i in range(len(board[0]))]
    for i in range(len(board) - 1, -1, -1):
        for j in range(len(board[0])):
            if board[i][j] != 0:
                board_stack[j].append(board[i][j])
    result = 0
    moves_stack = []
    for i in moves:
        if len(board_stack[i - 1]) > 0:
            tmp = board_stack[i - 1].pop()
            if len(moves_stack) > 0 and tmp == moves_stack[-1]:
                moves_stack.pop()
                result += 2
            else:
                moves_stack.append(tmp)
    return result
