# 네트워크

def dfs(n, computers, visited, idx):
    visited[idx] = True
    for i in range(n):
        if computers[idx][i] and i != idx:
            if not visited[i]:
                dfs(n, computers, visited, i)


def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(n, computers, visited, i)
            answer += 1
    return answer
