def solution(n):
    array = [0]* (n+1)
    for i in range(n+1):
        if i <= 1:
            array[i] = 1
        else:
            array[i] = array[i-2] + array[i-1]
    
    return array[n] % 1234567