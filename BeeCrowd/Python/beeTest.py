# -*- coding: utf-8 -*-
N, M = map(int, input().split())

matriz = [list(input()) for _ in range(N)]

inicio = matriz[0].index('o')

colunas_chuvosas = [inicio]

for linha in range (0, N):
  coluna = colunas_chuvosas[0]
  descendo = True
  if linha % 2 == 1: # Se a linha for impar so chove se tem goteira logo em cima
    matriz[linha] = [('o' if indice in colunas_chuvosas and matriz[linha][indice] != '#' else matriz[linha][indice])for indice in range(M)]# Pra cada elemento da linha (lista)
    continue
  while True:
    if matriz[linha-1][coluna] == 'o':
      matriz[linha][coluna] = 'o'
      if not coluna in colunas_chuvosas: colunas_chuvosas.append(coluna)
      if coluna > 0 and descendo: #se ainda nao tiver no final
        coluna -= 1
      else:
        if coluna == N-1: #se tiver chegado no final
          break
        #senao
        coluna+=1
        descendo = False
      continue
    if linha < N-1:
      if (matriz[linha][coluna-1] == 'o' and matriz[linha+1][coluna-1] == '#') or coluna == inicio:
        if not coluna in colunas_chuvosas: colunas_chuvosas.append(coluna)
        matriz[linha][coluna-1] = 'o'
        if coluna > 0 and descendo and matriz[linha+1][coluna] == '#': #se ainda nao tiver no final
          coluna -= 1
        else:
          if coluna == N-1: #se tiver chegado no final
            break
          #senao
          coluna+=1
          descendo = False
        continue
      elif (matriz[linha][coluna+1] == 'o' and matriz[linha+1][coluna+1] == '#') or coluna == inicio:
        if not coluna in colunas_chuvosas: colunas_chuvosas.append(coluna)
        matriz[linha][coluna] = 'o'
        if coluna > 0 and descendo: #se ainda nao tiver no final
          coluna -= 1
        else:
          if coluna == N-1: #se tiver chegado no final
            break
          #senao
          coluna+=1
          descendo = False
        continue
      else:
        break
    else: 
      break
print('\n'.join(map(str, matriz)))
