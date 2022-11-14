from itertools import permutations
def solution(babbling):
    
    word = ['aya', 'ye','woo','ma']
    words = set()
    for i in range(1, 5):
        for lst in permutations(word, i):
            words.add(''.join(lst))
    result= 0
    for b in babbling:
        if b in words:
            result += 1
    return result