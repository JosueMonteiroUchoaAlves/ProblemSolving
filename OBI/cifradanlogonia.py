palavra = str(input())

alfabeto = "abcdefghijklmnopqrstuvwxyz"
vogais = "aeiou"
consoantes = "bcdfghjklmnpqrstvwxyz"
posvogais = [0, 4, 8, 14, 20]
cifra = ""

"""
para cada letra
  se for vogal:
    apenas adiciona a vogal
  senao
    adiciona a consoante
    
    procura a posicao dela no alfabeto
    acha a vogal mais proxima
    adiciona a vogal mais proxima
    
    se for z
      adiciona z
    senao
      procura a proxima consoante (a letra + i na lista de consoantes)
      adiciona a consoante

"""

for letra in palavra:
  if letra in vogais:
    cifra = cifra + letra
  else:
    cifra = cifra+letra
    posicaoletra = alfabeto.find(letra)
    # A função sempre guardar o menor numero da diferenca entre posvogais e a posicao da letra
    # "ah esse é a menor diferenca, então ela vai ser a minima..." e assim vai
    vogalmaisproxima = min(posvogais, key=lambda x: abs(x-posicaoletra))
    cifra = cifra + alfabeto[vogalmaisproxima]
    
    if letra == "z":
      cifra = cifra + "z"
    else:
      posicaoconsoante= consoantes.find(letra)
      cifra = cifra + consoantes[posicaoconsoante+1]
    
print(cifra)
