# 뉴스 클러스터링

def solution(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    lst1 = [str1[i:i+2] if i < len1 - 1 else str1[i:] for i in range(len1 - 1)]
    lst1 = [i.lower() for i in lst1 if i.isalpha()]
    lst2 = [str2[i:i+2] if i < len2 - 1 else str2[i:] for i in range(len2 - 1)]
    lst2 = [i.lower() for i in lst2 if i.isalpha()]
    inter = []
    if len(lst1) < len(lst2):
        for i in lst1:
            if i in lst2:
                inter.append(i)
                lst2.remove(i)
    else:
        for i in lst2:
            if i in lst1:
                inter.append(i)
                lst1.remove(i)
    union = lst1 + lst2
    jaccard = 1 if len(union) == 0 else len(inter) / len(union)
    return int(jaccard * 65536)
