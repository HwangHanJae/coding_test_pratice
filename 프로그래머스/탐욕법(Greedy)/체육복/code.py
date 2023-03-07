def solution(n, lost, reserve):
    lost = {i : False for i in lost}
    
    reserve = set(reserve)
    temp = set()
    for i in reserve:
        if i in lost:
            temp.add(i)
            lost[i] = True
    reserve -= temp

    for i in reserve:
        if lost.get(i-1) == False:
            lost[i-1] = True
        elif lost.get(i+1) == False:
            lost[i+1] = True
    for i in lost:
        if lost.get(i) == False:
            n -= 1
            
    return n