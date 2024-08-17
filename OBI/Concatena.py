# OBI 2024
# SEGUNDA ETAPA | SECOND PHASE
# Only 40% correct because used too much memory.

n, q = map(int,input().split())
lista = list(map(int,input().split()))
ateAqui = [[] for _ in range(n-1)]
def func(nums, nova):
  somaTotal = 0
  for a in range(len(nums)-1):
    for z in range(a+1, len(nums)):
      somaTotal += ((nums[a]* 10) + nums[z]) + ((nums[z]* 10) + nums[a])
      nova[a].append(somaTotal)
    somaTotal = 0
  return nova

ateAqui = func(lista, ateAqui)
  

for _ in range(q):
  ini,end = map(int,input().split())
  result = 0
  for j in range(ini-1, end-1):
    result += ateAqui[j][(end-1)-j-1]
  print(result)
