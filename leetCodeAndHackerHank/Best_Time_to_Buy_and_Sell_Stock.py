# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
      max_profit = 0
      a,b = 0, 0
      while b < len(prices):
        if prices[a] < prices[b]:
          max_profit = max(max_profit, prices[b] - prices[a])
        else:
          a = b
        b+=1
      return max_profit  
