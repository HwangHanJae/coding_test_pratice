from collections import Counter
def solution(str1, str2):
    str1 = [str1[i:i+2].upper() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    str2 = [str2[i:i+2].upper() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    if len(str1) == 0 and len(str2) == 0:
        return 65536
    A = Counter(str1)
    B = Counter(str2)
    intersection = sum([min(A[key], B[key]) for key in (A&B)])
    union = sum([max(A[key], B[key]) for key in (A|B)])
    result = (intersection / union) * 65536
    
    return int(result)