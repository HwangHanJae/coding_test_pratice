n = int(input())
text = input()

A_text = 'ABC' * n
B_text ='BABC' * n
G_text = 'CCAABB' * n

dict = {
  "A" : 0,
  "B" : 0,
  "G" : 0
}
names = {
  "A" : 'Adrian',
  "B" : "Bruno",
  "G" : "Goran"
}
for i in range(len(text)):
  if text[i] == A_text[i]:
    dict["A"] += 1
  if text[i] == B_text[i]:
    dict['B'] += 1
  if text[i] == G_text[i]:
    dict['G'] += 1

max_count = max(dict.values())
result = [names[name] for name, count in dict.items() if count == max_count]
result.sort()
print(max_count)
for name in result:
  print(name)

