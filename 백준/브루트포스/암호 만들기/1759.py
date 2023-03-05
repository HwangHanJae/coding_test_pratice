from itertools import combinations

alphabet = set([chr(i) for i in range(ord('a'), ord('z')+1)])
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = list(alphabet - set(vowels))

l, c = map(int, input().split())
passwords = sorted(list(map(str, input().split())))
results = []
for password in combinations(passwords, l):
    vowel_count = 0
    cons_count = 0
    for c in password:
      if c in vowels:
        vowel_count += 1
        continue
      if c in consonants:
        cons_count += 1
    if vowel_count >= 1 and cons_count >= 2:
      results.append(''.join(password))

for result in results:
  print(result)

