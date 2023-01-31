def solution(numbers, hand):    
    result = ''
    coordinate = {
        1 : (0,3),
        2 : (1,3),
        3 : (2,3),
        4 : (0,2),
        5 : (1,2),
        6 : (2,2),
        7 : (0,1),
        8 : (1,1),
        9 : (2,1),
        0 : (1,0),
        '*' : (0,0),
        '#' : (2,0)
    }
    def distance(number, hand):
        x1, y1 = coordinate[number]
        x2, y2 = hand

        d = abs(x2-x1) + abs(y2-y1)
        return d
    
    left_hand = coordinate['*']
    right_hand = coordinate['#']
    
    for n in numbers:
        if n in (1,4,7):
            result += 'L'
            left_hand = coordinate[n]
        elif n in (3,6,9):
            result += 'R'
            right_hand = coordinate[n]
        elif n in (2,5,8,0):
            if distance(n, left_hand) < distance(n, right_hand):
                result += 'L'
                left_hand = coordinate[n]
            elif distance(n, left_hand) > distance(n, right_hand):
                result += 'R'
                right_hand = coordinate[n]
            else:
                if hand == 'left':
                    result += 'L'
                    left_hand = coordinate[n]
                else:
                    result += 'R'
                    right_hand = coordinate[n]
                
    
    return result

