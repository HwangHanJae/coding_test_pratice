def solution(n, arr1, arr2):
    results = []
    for i in range(n):
        result = ''
        arr1_b = bin(arr1[i])[2:]
        arr2_b = bin(arr2[i])[2:]
        if len(arr1_b) < n:
            arr1_b  = (n-len(arr1_b)) * '0' + arr1_b
        if len(arr2_b) < n:
            arr2_b  = (n-len(arr2_b)) * '0' + arr2_b
        for j in range(n):
            value = int(arr1_b[j]) + int(arr2_b[j])
            if value > 0:
                result += '#'
            else:
                result += ' '
        results.append(result)
    return results