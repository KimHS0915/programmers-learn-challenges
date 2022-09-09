# 신고 결과 받기

def solution(id_list, report, k):
    dic = {i: set() for i in id_list}
    for i in report:
        user, reported = i.split()
        dic[reported].add(user)
    mail_nums = {i: 0 for i in id_list}
    for ids in dic.values():
        if len(ids) >= k:
            for user_id in ids:
                mail_nums[user_id] += 1
    return list(mail_nums.values())
