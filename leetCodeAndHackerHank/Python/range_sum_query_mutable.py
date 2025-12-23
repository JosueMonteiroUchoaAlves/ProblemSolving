# https://leetcode.com/problems/range-sum-query-mutable/?envType=problem-list-v2&envId=binary-indexed-tree

from typing import List

# Fenwick tree

class NumArray:
    def __init__(self, nums: List[int]):
        # Variaveis
        self.Listnums = nums
        self.sumList = nums.copy() # Inicializando a lista de somas como uma cópia
        
        for indice, item in enumerate(self.sumList):
            indice += 1 # para parecer que a lista é indexada apartir do 1
            # proximoNoRange é o proximo lugar de acumular somas (que encontro de forma binaria)
            proximoNoRange = indice + (indice & -indice) #somo o ultimo bit ligado da var indice a ela msma
            if proximoNoRange <= len(self.sumList):
                self.sumList[proximoNoRange-1] +=  item

    def update(self, index: int, val: int) -> None:
        tamanhoSumList = len(self.sumList)
        numeroAnterior = self.Listnums[index]
        diferencaNovoValor = val - numeroAnterior 
        # Ex: val = 1 , anterior = 2. Uma diferenca de -1 tera que ser refletida
        # Ex2: val = 2 , anterior = 1. Uma diferenca de 1 tera que ser refletida
        # refletindo a mudanca tambem na lista de numeros (depois vou refletir na soma)
        self.Listnums[index] += diferencaNovoValor 
        # deixando no padrao fenwick para poder modificar os bits corretamente
        # porem na hora de mexer na lista mexe normalmente! tem que subtrair 1
        fenwickIndex = index + 1
        while fenwickIndex <= tamanhoSumList:
            self.sumList[fenwickIndex-1] += diferencaNovoValor
            fenwickIndex += fenwickIndex & -fenwickIndex # o proximo é a soma do index com seu bit menos significativo
        

    def sumRange(self, left: int, right: int) -> int:
        somaDoRangeRight = 0
        somaDoRangeLeft = 0
        # fenwick trees usam 1-index
        fenwickRight = right + 1
        while fenwickRight > 0 : # ele vai ate zero para acumular todas as somas ate la 
            somaDoRangeRight += self.sumList[fenwickRight-1] # lista usa 0-index, que é 1 a menos que o padrao fenwick
            fenwickRight -= (fenwickRight & -fenwickRight) # o proximo será: right - seu bit menos significativo
        
        # o left nao esta no "padrao fenwick" (somado com 1) pois se estiver ele tambem sera excluido da soma
        # depois preciso saber quais somas entre left e zero somei (pois nao quero elas)
        while left > 0: # pois o minimo do meu left (no padrao do fenwick) está como 1
            somaDoRangeLeft += self.sumList[left-1] # lista usa 0-index
            left -= (left & -left) # o proximo será: left - seu bit menos significativo
        return somaDoRangeRight - somaDoRangeLeft
# Your NumArray object will be instantiated and called as such:
# primeiro loop de soma
#        0  1  2   3  4  5   6   7  8  9 10 11 12  13 14 
#nums = [5, 2, 9, -3, 5, 20, 10,-7, 2, 3,-4, 0,-2, 15, 5]
"""nums = [1,2,3,4]
obj = NumArray(nums)
print(obj.sumRange(1, 3))
index = 1
val = 2
obj.update(index,val)
print(obj.sumRange(0, 2))"""

print("*"*30)
# Caso de teste do LeetCode
nums = [7,2,7,2,0]
obj = NumArray(nums)

obj.update(4,6)
obj.update(0,2)
obj.update(0,9)
print("sumRange(4,4) =", obj.sumRange(4,4))  # esperado 6

obj.update(3,8)
print("sumRange(0,4) =", obj.sumRange(0,4))  # esperado 32

obj.update(4,1)
print("sumRange(0,3) =", obj.sumRange(0,3))  # esperado 26
print("sumRange(0,4) =", obj.sumRange(0,4))  # esperado 27

obj.update(0,4)


"""
left = 7
right = 13
primeiro loop (soma)
       |--------------------------------------------|
        0  1  2   3  4  5   6   7  8  9 10 11 12  13 14 
nums = [5, 2, 9, -3, 5, 20, 10,-7, 2, 3,-4, 0,-2, 15, 5]

Segundo loop loop (soma)
       |----------------------|
        0  1  2   3  4  5   6   7  8  9 10 11 12  13 14 
nums = [5, 2, 9, -3, 5, 20, 10,-7, 2, 3,-4, 0,-2, 15, 5]

subtraindo os dois:
Segundo loop loop (soma)
                               |--------------------|
        0  1  2   3  4  5   6   7  8  9 10 11 12  13 14 
nums = [5, 2, 9, -3, 5, 20, 10,-7, 2, 3,-4, 0,-2, 15, 5]
"""
