# 스킬트리

def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        tmp = ""
        for i in skill_tree:
            if i in skill:
                tmp += i
        if skill[:len(tmp)] == tmp:
            answer += 1
    return answer
