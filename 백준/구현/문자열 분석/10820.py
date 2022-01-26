import sys
input = sys.stdin.readline

while True:
    
    #몇개가 주어질지 안알려주었기 때문에
    #try ~ except 문을 사용
    try:
        low = 0
        up = 0
        num = 0
        space = 0

        s = input().rstrip("\n")
        if s == '':
            break
        for i in range(len(s)):
            if s[i].isupper():
                up+=1     

            elif s[i].islower():
                low+=1
            elif s[i].isnumeric():
                num+=1
            elif s[i].isspace():
                space +=1
        print(low, up, num, space)
    except EOFError:
        break


