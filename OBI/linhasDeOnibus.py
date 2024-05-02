# -*- coding: utf-8 -*-

NumTerminais, NumLinhas, TermOrigem, TermDestino =  map(int, input().split())

## Vou usar BFS
## Usei BFS mas não soube guardar o menor caminho e o programa está lento
## Devo mudar pra DFS e melhorar meu codigo para ele ser mais rapido
"""
Primeiro recebo todas as linhas
Segundo vejo as intersseções entre as linhas
depois faço um BFS por todas as combinações de linha
"""

TerminaisDasLinhas = []

linhaInicial = 0

for i in range(NumLinhas):
  TerminaisDasLinhas.append(tuple(map(int,input().split()))[1:])
  if TermOrigem in TerminaisDasLinhas[i]:
    linhaInicial = i
TerminaisEmComum = [[] for i in range(NumLinhas)] 
## print(linhaInicial)
for index, Linha in enumerate(TerminaisDasLinhas): # Passando por todas as linhas, pegando os terminais e o index
  for seguinte in range (0, NumLinhas): # Pegando todos os outros terminais
    if index != seguinte and set(Linha).intersection(set(TerminaisDasLinhas[seguinte])):
      TerminaisEmComum[index].append(seguinte) # Adicionando os que tem terminais em comum como ligados

## print(*TerminaisEmComum,sep='\n')

def ChecarTerminais():
  if TermDestino in TerminaisDasLinhas[linhaInicial]:
    if TermOrigem == TermDestino:
      return 0
    return 1
    ## Se ele ja nao tava no destino, então retorna
    ## que ele teve que fazer no máximo 1 viajem pq 
    ## já tinha a parada na mesma linha
  linhasNecessarias = 0
  passou=[False]*NumLinhas
  passou[linhaInicial] = True
  pilha = [*TerminaisEmComum[linhaInicial]] 
  ## print("pilha:",pilha)
  ## vou visitar inicialmente as linhas da primeira linha
  while pilha:
    visitando = pilha[0]
    ## pra cada ligação que eu acessar, preciso
    ## Incrementar o numero de linhas necessarias
    if TermDestino in TerminaisDasLinhas[pilha[0]]: 
      return linhasNecessarias + 1
      ## Retorna o numero de linhas necessarias + aquela acessada agroa
    else:
      for vizinho in TerminaisEmComum[visitando]:
        if not passou[vizinho]:
          passou[vizinho] = True
          pilha.append(vizinho)
    linhasNecessarias += 1 
    pilha.pop(0)
print(ChecarTerminais())
