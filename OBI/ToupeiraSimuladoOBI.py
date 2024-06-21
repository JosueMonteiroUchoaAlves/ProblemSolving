def busca(lista, tuneis):
  for i in range(len(lista)-1):
    if lista[i+1] not in tuneis[lista[i]]:
      return 0
  return 1

X = 0
Y = 0
S, T = 0, 0
casos= 0
N= 0
var= 0
caso = []
total = 0
S, T = map(int,input().split())
tuneis = [[]for i in range(S+1)]
for _ in range(T):
  X, Y = map(int,input().split())
  tuneis[X].append(Y);
  tuneis[Y].append(X);

casos = int(input()) 
for i in range (casos):
  caso = list(map(int, input().split()))
  caso.pop(0)
  total += busca(caso, tuneis)
  
print(total)
