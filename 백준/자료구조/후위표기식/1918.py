import sys
from collections import deque
input = sys.stdin.readline

data = input().rstrip()

results = ''
stack = deque()

for word in data:
    #입력된 단어가 알파벳인지 구분
    #입력된 단어가 알파벳이라면 결과에 추가
    if word.isalpha():
        results += word
    else:
        #입력된 단어가 "("라면
        if word == "(":
            # 스택에 "("을 추가
            stack.append(word)
        #입력된 단어가 "*" or "/"라면
        elif word == "*" or word == "/":
            #반복문을 도는데 이때 반복문은 stack이 비어있지 않거나
            #stack의 가장 마지막에 등록된 값이 "*"or"/" 이어야 한다
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                results += stack.pop()          # 결과에 stack의 최상단 값을 pop하고 등록
            #입력된 단어가 "*" or "/" 일때 stack에 추가
            stack.append(word)
        #입력된 단어가 "+" or "-" 라면
        elif word == "+" or word == "-":
            # 반복문을 도는데 이때 반복문은 stack이 비어있지 않거나
            # stack의 최단값이 "(" 아니어야 한다.
            while stack and stack[-1] != "(":
                results += stack.pop()      # 결과에 stack의 최상단 값을 pop하고 등록
            #입력된 단어가 "+" or "-" 일때 stack에 추가
            stack.append(word)
        #입력된 단어가 ")"라면
        elif word  == ")":
            # 반복문을 도는데 이때 반복문은 stack이 비어있지 않거나
            # stack의 최단값이 "(" 아니어야 한다.
            while stack and stack[-1] != "(":
                results += stack.pop() # 결과에 stack의 최상단 값을 pop하고 등록
        
            stack.pop()

#stack을 돌면서 남아있는 값을 결과에 추가
while stack:
    results += stack.pop()

print(results)









