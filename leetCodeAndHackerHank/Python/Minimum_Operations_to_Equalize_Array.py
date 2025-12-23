# https://leetcode.com/contest/weekly-contest-466/problems/minimum-operations-to-equalize-array/submissions/1762775499/
from typing import List

# Eu posso simplesmente fazer um "and" em todos os items
# se todos forem iguais nao preciso fazer, então o resultado pode ser 1 and ou nenhum
def minOperations(nums: List[int]) -> int:
    if nums.count(nums[0]) == len(nums):
        return 0
    return 1
print(minOperations([1,2,1]))
