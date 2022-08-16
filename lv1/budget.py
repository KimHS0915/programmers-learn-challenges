# 예산

def solution(d, budget):
    support = []
    for i in sorted(d):        
        if sum(support) + i > budget:
            break
        support.append(i)
    return len(support)