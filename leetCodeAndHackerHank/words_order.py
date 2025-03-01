words = dict()
n = int(input())

for _ in range(n):
  word = input()
  if words.get(word):
    words[word] += 1
  else:
    words[word] = 1

print(len(words))
print(*words.values())
