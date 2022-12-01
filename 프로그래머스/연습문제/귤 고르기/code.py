from collections import Counter
def solution(k, tangerine):
    counter =  Counter(tangerine)
    sorted = counter.most_common()
    result = set()
    for num, count in sorted:
        k -= count
        result.add(num)
        if k <= 0:
            break
    return len(result)
            
    
    