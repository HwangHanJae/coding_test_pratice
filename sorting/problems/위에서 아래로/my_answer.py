#내가 푼 것
n = int(input())
numbers = []
for i in range(n):
  numbers.append(int(input()))

numbers.sort(reverse=True)
for number in numbers:
  print(number, end=' ')
