result = 0
for _ in range(int(input())):
  student, apple = map(int, input().split())
  result += (apple % student)
print(result)
