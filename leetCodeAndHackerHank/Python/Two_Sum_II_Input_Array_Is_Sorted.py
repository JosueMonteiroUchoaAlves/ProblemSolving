# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# 167. Two Sum II - Input Array Is Sorted

def twoSum(numbers: list[int], target: int) -> list[int]:
  PointerA, PointerZ = 0, len(numbers)-1
  while PointerA < PointerZ:
    var = numbers[PointerA] + numbers[PointerZ]
    if var == target:
      return [PointerA+1, PointerZ+1]
    if var > target:
      PointerZ -= 1
    else:
      PointerA +=1
      
