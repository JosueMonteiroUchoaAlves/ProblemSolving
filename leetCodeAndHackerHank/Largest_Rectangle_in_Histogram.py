# https://leetcode.com/problems/largest-rectangle-in-histogram/
# 84. Largest Rectangle in Histogram

## Probably I'll made a cleaner code after.##

class Solution:
  def largestRectangleArea(self, heights: list[int]) -> int:
    stack=[]
    maxSize = -1
    actualStarts = -1
    quantValues = len(heights)
    for index, value in enumerate(heights):
        actualStarts = index
        while stack and value<stack[-1][0]:
            var = stack.pop()
            varArea = var[0] * (index-var[1])
            maxSize = max(varArea,maxSize)
            actualStarts = var[1]
        stack.append([value, actualStarts])
    for item in stack:
      varArea = item[0] * (quantValues-item[1])
      maxSize = max(varArea,maxSize)
    return maxSize  
