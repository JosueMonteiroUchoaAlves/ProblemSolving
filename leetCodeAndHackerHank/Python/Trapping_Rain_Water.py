# https://leetcode.com/problems/trapping-rain-water/description/
# 42. Trapping Rain Water

class Solution:
    def trap(self, height: list[int]) -> int:
      maxL = -1
      maxR = -1
      water = 0
      L, R = 0, len(height)-1
      
      while L < R:
        if height[L] < height[R]:
          maxL = max(maxL, height[L])
          water += maxL - height[L] 
          L += 1
        else:
          maxR = max(maxR, height[R])
          water += maxR - height[R] 
          R -= 1
      return water
