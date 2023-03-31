def solution(name, yearning, photo):
    result = []
    score = {n: y for n, y in zip(name, yearning)}
    for i in range(len(photo)):
        sum_value = sum([score.get(name, 0) for name in photo[i]])
        result.append(sum_value)
    return result
        
            