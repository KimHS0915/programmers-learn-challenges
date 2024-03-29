# 다리를 지나는 트럭

def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = [0] * bridge_length
    while q:
        q.pop(0)
        if truck_weights:
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
        answer += 1
    return answer
