def solution(k, score):
    lst = []
    result = []
    for i in score:
        lst.append(i)
        lst.sort(reverse=True)
        lst = lst[:k]
        result.append(lst[-1])
        
    return result
        