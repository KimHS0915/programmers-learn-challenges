# 비밀지도

def solution(n, arr1, arr2):
    answer = []
    arr = [format(arr1[i] | arr2[i], "b").zfill(n) for i in range(n)]
    for b in arr:
        answer.append("".join(["#" if i == "1" else " " for i in b]))
    return answer
