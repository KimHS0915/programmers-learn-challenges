# 행렬의 곱셈

def solution(arr1, arr2):
    arr1_row = len(arr1)
    arr2_col = len(arr2[0])
    answer = [[0] * arr2_col for _ in range(arr1_row)]
    for i in range(arr1_row):
        for j in range(len(arr2)):
            for k in range(arr2_col):
                answer[i][k] += arr1[i][j] * arr2[j][k]
    return answer
