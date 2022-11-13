# 입국심사

def solution(n, times):
    answer = 0
    low, high = 1, max(times) * n
    while low <= high:
        mid = (low + high) // 2
        total_people = 0
        for time in times:
            total_people += mid // time
            if total_people >= n:
                break
        if total_people >= n:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
    return answer
