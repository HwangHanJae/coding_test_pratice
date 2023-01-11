from datetime import datetime
def solution(today, terms, privacies):
    today_year = int(today.split('.')[0])
    today_month = int(today.split('.')[1])
    today_day = int(today.split('.')[2])
    #terms 딕셔너리로 변경
    term = {}
    result = []
    for i in range(len(terms)):
        t = terms[i].split()
        term[t[0]] = int(t[1])
    
    for i, privacy in enumerate(privacies):
        privacy = privacy.split()
        kind = privacy[1]
        privacy = privacy[0].split('.')
        year = int(privacy[0])
        month = int(privacy[1])
        day = int(privacy[2])
        
        #month 계산
        month += term[kind]
        while month > 12:
            month -= 12
            year += 1
        
        #day 계산
        day -= 1
        if day == 0:
            month -= 1
            day = 28
        
        if month == 0:
            month = 12
            year -= 1
        
        if datetime(today_year, today_month, today_day) > datetime(year, month, day):
            result.append(i+1)
            
    return result
        
        
        