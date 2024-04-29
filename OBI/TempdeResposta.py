registros = int(input())

# contato, pendente?
contatos = dict()

for i in range(registros):
  acao, valor2 = input().split()
  tempo = 1
  if acao == 'T':
    tempo=int(valor2)
  elif acao == "R":
    if not contatos.get(valor2): # se o contato nao estiver no dicionario
      contatos.update({valor2:[True, 0]}) #adiciona com tempo 0
    else:
      contatos[valor2][0] = True # Fala que ele ta pendente denovo
  elif acao == 'E':
    contatos[valor2][0] = False # marcar como respondido (False)
    
  for key in contatos.keys(): #vai pegar todos os pendentes e aumentar o tempo deles
    if contatos[key][0] == True and ((acao == "R" and valor2 != key) or acao != "R"): #se estiver pendente
      contatos[key][1] += tempo

    
contatos = dict(sorted(contatos.items()))
for key in contatos.keys():
  print(key, contatos[key][1] if contatos[key][0] == False else "-1")
