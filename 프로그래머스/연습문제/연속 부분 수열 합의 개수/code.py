def solution(elements):
    result = set()
    len_ = len(elements)
    elements = elements * 2
    for l in range(1, len_+1):
        for i in range(len(elements)):
            result.add(sum(elements[i:l+i]))
            
    return len(result)