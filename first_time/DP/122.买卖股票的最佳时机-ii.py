#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start

# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/solution/yi-ge-tong-yong-fang-fa-tuan-mie-6-dao-gu-piao-wen/
# class Solution:
#     def maxProfit(self, prices):
#         maxProfit = 0
#         len_prices = len(prices)
#         for i in range(len_prices-1):
#             if prices[i+1] - prices[i] > 0:
#                 maxProfit += (prices[i+1] - prices[i])
#         return maxProfit

class Solution:
    def maxProfit(self, prices):
        dp = [[0, 0] for i in range(len(prices))]
        # 持有股票
        dp[0][0] = -prices[0]
        # 不持有股票
        dp[0][1] = 0
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])
        return dp[-1][1]
        
# @lc code=end

