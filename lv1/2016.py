# 2016년

from datetime import date

def solution(a, b):
    days = {0:'FRI', 1:'SAT', 2:'SUN', 3:'MON', 4:'TUE', 5:'WED', 6:'THU'}
    key = (date(2016, a, b) - date(2016, 1, 1)).days % 7
    return days[key]