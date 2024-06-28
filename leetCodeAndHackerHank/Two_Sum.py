#https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dicionario = {}
        for index, item in enumerate(nums):
            if target-item in dicionario:
                return [index, dicionario[target-item]]
            elif item not in dicionario:
                dicionario[item] = index
