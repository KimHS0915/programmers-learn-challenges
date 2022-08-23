# 영어 끝말잇기

def solution(n, words):
    lst = []
    for i in range(len(words)):
        if words[i] in lst or (i > 0 and words[i - 1][-1] != words[i][0]):
            return [i % n + 1, i // n + 1]
        lst.append(words[i])
    return [0, 0]
