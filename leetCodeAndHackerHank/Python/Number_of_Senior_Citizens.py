# https://leetcode.com/problems/number-of-senior-citizens/description/?envType=daily-question&envId=2024-08-01
# 2678. Number of Senior Citizens
class Solution:
    def countSeniors(self, details: list[str]) -> int:
      total = 0
      for guy in details:
        if int(guy[11:13]) > 60: total +=1
      return total
