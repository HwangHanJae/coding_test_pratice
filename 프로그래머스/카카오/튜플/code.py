def solution(s):
    result = []
    array = []
    s = s[2:-2]
    array = s.split('},{')
    array.sort(key=lambda x: len(x))
    for lst in array:
        lst = lst.split(',')
        for number in list(lst):
            if int(number) in result:
                pass
            else:
                result.append(int(number))
            
    
    return result
