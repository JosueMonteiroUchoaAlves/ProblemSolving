# https://leetcode.com/problems/3sum/
# 15. 3Sum

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        combinations = []
        
        for index, a in enumerate(nums):
          if index > 0 and a == nums[index-1]:
              continue
          l,r = index + 1, len(nums) - 1
          while l < r:
            sum_ = a + nums[l] + nums[r]
            if sum_ < 0:
              l += 1
            elif sum_ > 0:
              r -= 1
            else:
              combinations.append([a, nums[l], nums[r]])
              l +=1
              while nums[r] == nums[r-1] and l < r:
                l += 1
        return combinations
