def solution(brown, yellow):
    total = brown + yellow
    
    for i in range(1, brown+1):
        for j in range(1, i+1):
            if (i * j) == total:
                if 2*(i+j-2) == brown:
                    return [i, j]