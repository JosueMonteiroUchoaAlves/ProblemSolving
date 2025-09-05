# https://leetcode.com/contest/weekly-contest-465/problems/restore-finishing-order/submissions/1759931456/

class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        ans = []
        for item in order:
          if item in friends:
            ans.append(item)
        return ans
