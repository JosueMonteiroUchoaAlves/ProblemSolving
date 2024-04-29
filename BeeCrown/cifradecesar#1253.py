possibilidades = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

## CODE FULLY WORKING

n = int(input())
respostas = []
for _ in range(n):
  codigo = input()
  i = int(input())
  decifrado = "".join([possibilidades[possibilidades.find(char)-i+26] for char in codigo])
  respostas.append(decifrado)

print('\n'.join(map(str, respostas)))
