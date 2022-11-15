def solution(n):
    numbers = [i for i in range(1, (n // 2) + 2)]
    result = set()
    for i in range(len(numbers)+1):
        for j in range(i+1, len(numbers)+1):
            if sum(numbers[i:j]) == n:
                result.add(tuple(numbers[i:j]))
            elif sum(numbers[i:j]) > n:
                break
                
    if (n, ) not in result:
        return len(result) + 1
    
    return len(result)