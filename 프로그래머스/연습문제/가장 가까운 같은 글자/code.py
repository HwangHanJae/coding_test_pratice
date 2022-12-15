def solution(s):
    dic = {}
    result = []
    for i, c in enumerate(s):
        if dic.get(c) == None:
            result.append(-1)
        else:
            result.append(i - dic[c])
        dic[c] = i
            
    return result