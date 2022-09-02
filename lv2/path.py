# 방문 길이

def solution(dirs):
    coords = [(0, 0)]
    paths = []
    move = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
    for i in dirs:
        curr = (coords[-1][0] + move[i][0], coords[-1][1] + move[i][1])
        if abs(curr[0]) <= 5 and abs(curr[1]) <= 5:
            path = (curr, coords[-1]) if curr < coords[-1] else (coords[-1], curr)
            paths.append(path)
            coords.append(curr)
    return len(set(paths))
