# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
# 153. Find Minimum in Rotated Sorted Array
class Solution:
    def findMin(self, nums: List[int]) -> int:
      if len(nums) == 1:
        return nums[0]
      left, right = 0, len(nums)-1
      lower = float('inf')
      while left < right:
        mid = (left+right)//2
        if nums[left] < nums[right]:
          right= mid-1
          lower = nums[left]
          continue
        if nums[left] > nums[right] and nums[mid] < nums[right]:
          right= mid
          lower = nums[mid]
        else:
          left = mid+1
          lower = nums[right]
      return lower
