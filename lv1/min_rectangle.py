# 최소직사각형

def solution(sizes):
    w = 0
    h = 0
    for size in sizes:
        if size[0] < size[1]:
            size[0], size[1] = size[1], size[0]
        if size[0] > w:
            w = size[0]
        if size[1] > h:
            h = size[1]
    return w * h
