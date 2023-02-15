import math

def is_prime(number):
  for i in range(2, int(math.sqrt(number))+1):
      if number % i == 0:
        return False
  return True
a, b = map(int, input().split())
b = min(10000000, b)
palindrome = [i for i in range(a, b+1) if str(i) == str(i)[::-1]]
for number in palindrome:
  if is_prime(number):
      print(number)
print(-1)