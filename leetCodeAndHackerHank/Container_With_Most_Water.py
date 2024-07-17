# https://leetcode.com/problems/container-with-most-water/submissions/1323526920/
# 11. Container With Most Water
class Solution:
    def maxArea(self, height: list[int]) -> int:
      PointerA, PointerZ = 0, len(height)-1
      Biggest = -1
      while PointerA < PointerZ:
        Biggest = max(Biggest, (PointerZ - PointerA ) * min(height[PointerA], height[PointerZ]) )
        if height[PointerA] < height[PointerZ]:
          PointerA += 1 
        else: 
          PointerZ -= 1 
      return Biggest
