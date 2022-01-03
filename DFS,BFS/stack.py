#스택 예제
stack = []

stack.append(54)
stack.append(65)
stack.append(83)
stack.pop()
stack.append(57)

print(stack) #최하단 원소부터 출력
print(stack[::-1]) #최상단 원소부터 출력

#파이썬에서 별도의 라이브러리 없이 append(), pop()함수를 이용하면 스택을 구현 가능
