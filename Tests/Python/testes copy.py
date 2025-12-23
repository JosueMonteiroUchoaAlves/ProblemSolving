def passando(matrix:list[str], N):
  a = 0
  newmatrix = matrix.copy()
  for i in range(1, N):
    for j in range(1, N):
      a = (int(matrix[i-1][j-1])+int(matrix[i-1][j])+int(matrix[i-1][j+1])+int(matrix[i][j-1])+int(matrix[i][j+1])++int(matrix[i+1][j-1])+int(matrix[i+1][j])+int(matrix[i+1][j+1]))
      print(a)
      if a == 3 and matrix[i][j] == "0":
        newmatrix[i+1] = "".join(matrix[i][k] if k != j+1 else "1" for k in range(N+2) )
        continue
      if matrix[i][j] == "0":
        continue
      if a in [2, 3] and matrix[i][j] == "1":
        newmatrix[i] =  "".join(matrix[i][k] if k != j+1 else "1" for k in range(N+2) )
      else: 
        newmatrix[i] =  "".join(matrix[i][k] if k != j+1 else "0" for k in range(N+2) )
  print(newmatrix)
  return newmatrix
N, interacoes = map(int, input().split())

matriz = ["0"*(N+2) for _ in range(N+2)]
print(*matriz)
palavra = ""

for i in range(N):
  palavra = input()
  matriz[i+1] = palavra.center(N+2, "0")
for i in range(interacoes):
  matriz = passando(matriz, N)
print(*matriz, sep="\n")
