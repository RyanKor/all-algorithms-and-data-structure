import datetime
def solution(a, b):
    answer = ''
    days = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    if datetime.date(2016,a,b).weekday() == 6:
        answer = days[0]
    else:
        answer = days[datetime.date(2016,a,b).weekday()+1]
    return answer