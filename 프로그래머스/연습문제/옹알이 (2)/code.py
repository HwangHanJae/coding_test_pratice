def solution(babbling):
    speak = ['aya','ye','woo','ma']
    result = 0
    for b in babbling:
        for i in range(len(speak)):
            if speak[i] * 2 not in b:
                b = b.replace(speak[i], ' ')
        if b.strip() == '':
            result += 1
        
    return result