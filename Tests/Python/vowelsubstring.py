from Tests.codetimer import clock

# Chamo meu decorador
#@clock
def findSubstring(s, k):
  string = list(s)
  biggest = "Not found!"
  vowelsonbiggest = 0
  for i in range(0, len(s)-k):
    contagem = string[i:i+k].count('a')+string[i:i+k].count('e')+string[i:i+k].count('i')+string[i:i+k].count('o')+string[i:i+k].count('u')
    if vowelsonbiggest < contagem:
      biggest = "".join(string[i:i+k])
      vowelsonbiggest = contagem
  return biggest


print(findSubstring("kmtgbioqwoeaeiouirnverynvey", 5))
