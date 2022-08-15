# 폰켓몬

def solution(nums):
    nums_len = len(nums)
    answer = nums_len / 2
    unique_nums_len = len(list(set(nums)))
    if unique_nums_len < answer:
        answer = unique_nums_len    
    return answer