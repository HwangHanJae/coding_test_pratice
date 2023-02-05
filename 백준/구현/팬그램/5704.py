import sys
while True:
  case = sys.stdin.readline().strip()
  if case == '*':
    break
  alphabet = set(chr(c) for c in range(ord('a'), ord('z')+1))
  for c in case:
    alphabet = alphabet - {c}
  if len(alphabet) > 0:
    print('N')
  else:
    print('Y')