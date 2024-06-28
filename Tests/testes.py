words =[1, 1, 3, 3, 2]
def topKFrequent(nums:list[int], k):
  dicionario = {}
  nums.sort()
  for item in nums:
    if item in dicionario:
      dicionario[item] += 1
    elif item not in dicionario:
      dicionario[item] = 1
  lista_do_dicionario = sorted(dicionario, key=lambda item: dicionario[item])
  return lista_do_dicionario[len(lista_do_dicionario)-k:]

print(topKFrequent(words, 2))

