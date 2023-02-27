def solve(test_case):
  #condition1
  for i in vowel:
    if i in test_case:
      break
  else:
    return False
  #condition2
  for i in range(len(test_case)-2):
    case = test_case[i:i+3]
    if condition2(case):
      pass
    else:
      return False
  #condition3
  for i in range(len(test_case)-1):
    case = test_case[i:i+2]
    if condition3(case):
      pass
    else:
      return False
    
  return True

def condition2(case):
  vowel_count = 0
  cons_count = 0
  for i in case:
    if i in vowel:
      vowel_count += 1
    if i in cons:
      cons_count += 1
  if vowel_count == len(case) or cons_count == len(case):
    return False
  return True

def condition3(case):
  if case == 'ee' or case == 'oo':
    return True
  if case[0] == case[1]:
    return False
  return True

def acceptable(word, flag):
  if flag:
    return f"<{word}> is acceptable."
  else:
    return f"<{word}> is not acceptable."
  

alphabet = [chr(c) for c in range(ord('a'), ord('z')+1)]
vowel = ['a','e','i','o','u']
cons = list(set(alphabet) - set(vowel))

while True:
  test_case = input()
  if len(test_case) == 1:
    if test_case in vowel:
      print(acceptable(test_case, True))
      continue
    else:
      print(acceptable(test_case, False))
      continue
  if test_case == 'end':
    break
  flag = solve(test_case)
  print(acceptable(test_case, flag))