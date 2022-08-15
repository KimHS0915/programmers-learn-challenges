# K번째수

def solution(array, commands):
    answer = []
    for command in commands:
        start = command[0] - 1
        end = command[1]
        idx = command[2] - 1
        answer.append(sorted(array[start:end])[idx])
    return answer