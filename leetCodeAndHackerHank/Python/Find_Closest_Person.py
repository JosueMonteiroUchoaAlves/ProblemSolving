# https://leetcode.com/problems/find-closest-person/

class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
      xDistance = abs(z - x)
      yDistance = abs(z - y)
      if xDistance > yDistance:
        return 2 
      elif xDistance == yDistance :
        return 0 
      else: 
        return 1 
