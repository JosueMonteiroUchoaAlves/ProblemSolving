#https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dicionario = {}
        nums.sort()
        for item in nums:
            if item in dicionario:
                dicionario[item] += 1
            elif item not in dicionario:
                dicionario[item] = 1
        lista_do_dicionario = sorted(dicionario, key=lambda item: dicionario[item])
        return lista_do_dicionario[len(lista_do_dicionario)-k:]
