#곱하기 혹은 더하기
s = list(map(int, input()))
#정렬
result = s[0]
for i in range(1, len(s)):
    n = s[i]
    if n <= 1 or result<=1:
        result += n
    else:
        result *= n
print(result)
    
