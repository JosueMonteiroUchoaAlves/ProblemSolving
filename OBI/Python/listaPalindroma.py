n = int(input())
v = list(map(int, input().split()))

i = 0          # Apontando para o primeiro item da lista
j = n - 1      # Apontando para o último
op = 0         # Número de operações
se = v[i]      # Mantém a soma das posições à esquerda
sd = v[j]      # Mantém a soma das posições à direita

while i <= j:
    if se == sd:
        # Se as somas coincidem, não precisamos fazer uma operação, pois
        # os elementos opostos são iguais (ou já conseguimos igualá-los)
        i += 1
        j -= 1
        se = v[i]
        sd = v[j]
    elif se < sd:
        # Se a soma da esquerda é menor, então somamos a posição
        # da esquerda com a próxima, esperando nos igualar à soma da direita
        i += 1
        se += v[i]
        op += 1
        if i == j:
            break
    else:
        # Se a soma da direita é menor, a ideia é análoga ao item anterior
        j -= 1
        sd += v[j]
        op += 1
        if i == j:
            break

print(op)
