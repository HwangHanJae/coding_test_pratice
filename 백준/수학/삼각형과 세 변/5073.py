while True:
  data = list(map(int, input().split()))
  if sum(data) == 0:
    break
  #가장 긴 변의 길이가 다른 두 변의 길이의 합보다
  #크거나 같다면 Invalid
  if max(data) >= sum(data) - max(data):
    print('Invalid')
    continue
  if len(set(data)) == 1:
    print('Equilateral')
  elif len(set(data)) == 2:
    print('Isosceles')
  elif len(set(data)) == 3:
    print('Scalene')