from codetimer import clock

with open("data.txt", "r") as archive:
    data = archive.read().split(", ")
data = [int(number) for number in data]
print(data, type(data))
pass

###################TESTE-1#######################
"""_summary_
  Testando percorrer listas usando o enumerante para contar o index enquanto acessa os dados
  
  resultados:
  
  A funcao test_1 executou em          0.00049 segundos
  A funcao test_1_improved executou em 0.00078 segundos
  
  NÃO HOUVE MELHORA
"""
@clock
def test_1():
  for i in range(len(data)):
    if i % 2 == 0:
      data[i] = 0  
@clock
def test_1_improved():
  for index, i in enumerate(data):
    if i % 2 == 0:
      data[index] = 0
      
test_1()
test_1_improved()
#################################################
# | #                                       # | #
# | #                                       # | # 
###################TESTE-2#######################
"""_summary_
  Testando se usar compressão de listas pode ajudar a melhorar a performance
  
  resultados:
  
  A funcao test_2 executou em          0.00128 segundos
  A funcao test_2_improved executou em 0.00085 segundos
  
  HOUVE MELHORA SIGNIFICATIVA
"""
@clock
def test_2():
  lista = []
  for i in range(40000):
    lista.append(i)
    
@clock
def test_2_improved():
  lista = [i for i in range(40000)]
  
test_2()
test_2_improved()
#################################################
# | #                                       # | #
# | #                                       # | # 
###################TESTE-3#######################
"""_summary_
  Testando se usar geradores no lugar de listas pode ajudar a melhorar a performance.
  
  resultados:
  
A funcao test_3 executou em          0.001007 segundos
A funcao test_3_improved executou em 0.001807 segundos
  
  NÃO HÁ MELHORA NO TEMPO, PORÉM O USO DE MEMÓRIA É SIGNFICATIVAMENTE REDUZIDO.
  OS TEMPOS SÃO MAIS CONSTANTES COM O GERADOR DO QUE NA LISTA, PORÉM A LISTA SEMPRE SAI GANHANDO
"""
@clock
def test_3():
  lista = [i for i in range(40000)]
  print(sum(lista))
    
@clock
def test_3_improved():
  gerador = (i for i in range(40000))
  print(sum(gerador))
  
test_3()
test_3_improved()
#################################################
# | #                                       # | #
# | #                                       # | # 
###################TESTE-4#######################
"""_summary_
  Substituir variaveis globais por locais
  
  resultados:
  
  A funcao test_4 executou em          0.4977 segundos
  A funcao test_4_improved executou em 0.4879 segundos
  
  HÁ POUCA OU NENHUMA MELHORA
"""
variavel_global = 10

@clock
def test_4():
  variavel = 1
  for _ in range(10**5):
    variavel *= variavel_global
    
@clock
def test_4_improved():
  variavel = 1
  variavel_local = variavel_global
  for _ in range(10**5):
    variavel *= variavel_local
  
test_4()
test_4_improved()
#################################################
# | #                                       # | #
# | #                                       # | # 
###################TESTE-5#######################
"""_summary_
  Substituindo o método de compressão de listas por criar um list(range()) - retorna uma lista com todos os numeros naquele range
  
  resultados:
  
  A funcao test_5 executou em          0.0009923 segundos
  A funcao test_5_improved executou em 0.0003637 segundos
  
  TEVE UMA MELHORA ALTAMENTE SIGNIFICATIVA
"""
variavel_global = 10

@clock
def test_5():
  lista = [i for i in range(40000)]
    
@clock
def test_5_improved():
  lista = list(range(40000))
  
test_5()
test_5_improved()
#################################################
# | #                                       # | #
# | #                                       # | # 
###################TESTE-6#######################
"""_summary_
  Usando unpacking para descompactar a lista ao imprimi-la vs mapear a lista (ambos melhores que passar de item em item)
  
  resultados:
  
  A funcao test_6 executou em          0.0462 segundos
  A funcao test_6_improved executou em 0.0227 segundos  
  
  TEVE UMA MELHORA ALTAMENTE SIGNIFICATIVA
"""
variavel_global = 10

@clock
def test_6():
  lista = list(range(500))
  print(*lista, sep='\n')
    
@clock
def test_6_improved():
  lista = list(range(500))
  print('\n'.join(map(str, lista)))
test_6()
test_6_improved()
#################################################
# | #                                       # | #
# | #                                       # | # 
###################TESTE-7#######################
## apenas um truque interessante para centralizar textos:
espac = 20
texto = "python"
print(f"{texto:^{espac}}") # centralizar com espaços
print(f"{texto:#^{espac}}") # centralizar com caracter
print(f"{texto:#>{espac}}") # deixar espaco a esquerda
print(f"{texto:#<{espac}}") # deixar espacoa  direita

#################################################
# | #                                       # | #
# | #                                       # | # 
