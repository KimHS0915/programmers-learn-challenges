# 문자열 압축

def solution(s):
    slen = len(s)
    if slen == 1:
        return 1
    results = []
    for i in range(1, slen // 2 + 1):
        cnt = 1
        comp_str = ""
        unit = s[:i]
        for j in range(i, slen, i):
            if unit == s[j:i + j]:
                cnt += 1
            else:
                comp_str += str(cnt) + unit if cnt > 1 else unit
                cnt = 1
                unit = s[j:i + j]
        comp_str += str(cnt) + unit if cnt > 1 else unit
        results.append(len(comp_str))
    return min(results)
