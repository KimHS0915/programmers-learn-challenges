# 파일명 정렬

def solution(files):
    for i, file in enumerate(files):
        n_start, t_start = 0, -1
        for j in range(len(file)):
            if n_start == 0 and file[j].isdigit():
                n_start = j
            elif n_start > 0 and not file[j].isdigit():
                t_start = j
                break
        number = file[n_start:t_start] if t_start != -1 else file[n_start:]
        files[i] = [file[:n_start].lower(), int(number), file]
    answer = [file[2] for file in sorted(files, key=lambda x: (x[0], x[1]))]
    return answer
