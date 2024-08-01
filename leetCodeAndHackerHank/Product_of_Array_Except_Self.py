#https://leetcode.com/problems/product-of-array-except-self/description/
# 238. Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      result = [1]*len(nums)
      product = 1
      
      for i in range(len(nums)):
          result[i] = product 
          product *= nums[i]
          
      product = 1
      for i in range(len(nums)-1, -1, -1):
          result[i] *= product 
          product *= nums[i]
      return result
  