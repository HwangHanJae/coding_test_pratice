from collections import Counter
def solution(want, number, discount):
    result= 0
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]
    total = sum(number)
    
    for i in range(len(discount)):
        items = discount[i:i+10]
        if len(items) < 10:
            return result
        elif dic == dict(Counter(items)):
            result +=1
    return result
