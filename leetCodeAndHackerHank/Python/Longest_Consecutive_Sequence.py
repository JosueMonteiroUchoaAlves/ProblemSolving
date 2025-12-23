# https://leetcode.com/problems/longest-consecutive-sequence/description/
# 128. Longest Consecutive Sequence

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
      nums = set(nums)
      max_sequence = 0
      sequence = 0
      for num in nums:
          if num-1 in nums: continue
          sequence = 1
          i = num+1
          while i in nums:
              sequence += 1
              i += 1
          max_sequence = max(max_sequence, sequence)
      return max_sequence
