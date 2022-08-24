# 오픈채팅방

def solution(record):
    record = [i.split(" ") for i in record]
    user = {i[1]: i[2] for i in record if i[0] != "Leave"}
    msg = {"Enter": "들어왔습니다.", "Leave": "나갔습니다."}
    return [f"{user[i[1]]}님이 {msg[i[0]]}" for i in record if i[0] != "Change"]
