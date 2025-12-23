# https://leetcode.com/problems/binary-search/description/
# 704. Binary Search

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        min_, max_ = 0, len(nums) -1
        mid = max_ // 2
        while min_ <= max_:
            if nums[mid] == target: return mid
            if nums[mid] > target: max_ = mid - 1
            if nums[mid] < target: min_ = mid + 1
            mid = (min_ + max_) // 2
        return -1
