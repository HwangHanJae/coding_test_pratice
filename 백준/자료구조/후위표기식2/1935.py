def cal(left, right, center):
        if center == '*':
            value=float(left) * float(right)
        elif center =='-':
            value = float(left) - float(right)
        elif center == '/':
            value = float(left) / float(right)
        else:
            value = float(left) + float(right)
        return value
n = int(input())
expression = str(input())
stack = []
dic = {}
for i in range(ord('A'), ord('A')+n):
    dic[chr(i)] = float(input())
op = ['*', '-', '+', '/']
for c in expression:
    stack.append(c)
    if c in op:
        center = stack.pop()
        right = stack.pop()
        left = stack.pop()
        if dic.get(left):
            left = dic[left]            
        if dic.get(right):
            right = dic[right]
        value = cal(left, right, center)
        stack.append(value)

print('{:.2f}'.format(round(stack[0], 2)))
