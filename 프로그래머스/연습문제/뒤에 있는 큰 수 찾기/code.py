def solution(numbers):
    stack = []
    result = [-1] * len(numbers)
    for i in range(len(numbers)-1, -1, -1):
        if stack == []:
            stack.append(numbers[i])
            continue
        while stack:
            s = stack.pop()
            if s > numbers[i]:
                result[i] = s
                stack.append(s)
                break 
        stack.append(numbers[i])     
    return result