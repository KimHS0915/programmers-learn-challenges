# 다트 게임

import re


def solution(dartResult):
    answer = []
    bonus = {"S": 1, "D": 2, "T": 3}
    option = {"*": 2, "#": -1, "": 1}
    tokens = re.findall("(\d+)([SDT])([*#]?)", dartResult)
    for i, v in enumerate(tokens):
        answer.append(int(v[0]) ** bonus[v[1]] * option[v[2]])
        if v[2] == "*" and i > 0:
            answer[i - 1] *= 2
    return sum(answer)
