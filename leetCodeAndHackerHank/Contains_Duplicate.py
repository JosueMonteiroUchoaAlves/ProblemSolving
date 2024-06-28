#https://leetcode.com/problems/contains-duplicate/description/
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        a=set()
        for i in nums:
            if i in a:
                return True
            a.add(i)
        return False
