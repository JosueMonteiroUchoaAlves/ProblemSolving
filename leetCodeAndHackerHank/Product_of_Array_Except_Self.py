#https://leetcode.com/problems/product-of-array-except-self/description/
lista = [-1,1,0,-3,3]
def productExceptSelf(nums: list[int]) -> list[int]:
    dicionario = {0:1}
    for num in range(1, len(nums)+1):
        dicionario[num] = 1
        dicionario[num] *= dicionario[0] * nums[0]
        for i in dicionario:
            if i != num:
                dicionario[i] *= num
    print(dicionario)
    
productExceptSelf(lista)
