#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices):
        maxProfit = 0
        len_prices = len(prices)
        for i in range(len_prices-1):
            if prices[i+1] - prices[i] > 0:
                maxProfit += (prices[i+1] - prices[i])
        return maxProfit
        
# @lc code=end

