def search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums)-1
    
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        
        # saber se estou na parte left
        # ex: [3,4,5,0,1,2] de 3 a 5 é a parte left (esquerda)
        if nums[l] <= nums[m]:
            # target menor que o meio
            if target < nums[m]:
                # E maior ou igual à left
                if target >= nums[l]:
                    # Vamos focar a busca na parte esquerda
                    r = m - 1
                # se, então, era menor ainda que left, ja que estamos na left, vamos para right
                else:
                    # ex: [3,4,5,0,1,2] O 0 é menor ainda que 3
                    l = m + 1 
            # target é maior que nums[mid]
            else:
                # como já estamos na parte esquerda (crescente e organizada) vamos para a right
                # ex: [3,4,5,6,7,0,1,2] se eu quisesse esse 7 ai, cairia nesse else que estamos!
                l = m + 1 
                
        # se não estamos com a parte organizada á esquerda
        # ex: [4,5,0,1,2,3] 
        else:
            # target maior que o meio
            if target > nums[m]:
                # ainda maior que a direita
                if target > nums[r]:
                    # só pode ta na esquerda
                    r = m-1
                # não era maior que a direita
                else:
                    # vamos procurar na direita, pois pode ser ela ou outro numero entre ela e o meio
                    l = m+1
            # não era maior que o meio
            else:
                # já não pode ser maior que ninguem na direita, pois ate la esta organizado em ordem crescente. então vamos para esquerda
                # então 
                r = m-1
    return -1
print(search([4,5,6,7,8,1,2,3],2))

# Se eu estiver na parte "left" do array, l <= m
# (a parte left é a parte organizada de forma crescente)
# Comecando pela right:
# [4,5,0,1,2,3] 
# Comecando pela left:
# [3,4,5,0,1,2] 
#  desta forma sei que entre l e m é "continuo"

""" 
Um array rotacionado VAI POSSUIR UM "PONTO DE QUEBRA"
Quando eu escolho um numero nesse array, ele vai estar antes, ou depois 
desse ponto de quebra, e ele não pode estar antes e depois dele ao mesmo tempo, 
isso é óbvio!

antes do ponto de quebra (marcado pelo asterisco), vai estar tudo organizado:

0 rotações (original, não rotacionado):
[1, 2, 3, 4, 5, 6, 7, 8]
-----------------------
1 rotação:
[2, 3, 4, 5, 6, 7, 8, 1]
---------------------*+
2 rotações:
[3, 4, 5, 6, 7, 8, 1, 2]
------------------*++++
3 rotações:
[4, 5, 6, 7, 8, 1, 2, 3]
---------------*+++++++
4 rotações:
[5, 6, 7, 8, 1, 2, 3, 4]
------------*++++++++++
5 rotações:
[6, 7, 8, 1, 2, 3, 4, 5]
---------*+++++++++++++
6 rotações:
[7, 8, 1, 2, 3, 4, 5, 6]
------*++++++++++++++++
7 rotações:
[8, 1, 2, 3, 4, 5, 6, 7]
---*+++++++++++++++++++

Veja que surge uma divisória entre 2 seções organizadas!

Se o left <= mid, quer dizer que meu mid está antes do ponto de quebra, e tudo
á esquerda está organizado, então é ali que faço minha comparação!

Se o left > mid, então entre left e mid há uma quebra! pois em ordem ascendente
todos os items entre left (inclusive) e mid deveriam ser menores ou iguais a mid!
Então de mid para right vai estar organizado, já que descobrimos que a quebra fica na left!
Então usamos isso para fazer nossa busca!
"""
