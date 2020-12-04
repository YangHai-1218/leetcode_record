#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        dp = [[0]*2 for _ in range(len(prices))]
        for i in range(len(prices)):
            if i == 0:
                dp[i][1] = -prices[i]
                dp[i][0] = 0
            else:
                dp[i][1] = max(dp[i-1][1], -prices[i])
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        return dp[-1][0]

# @lc code=end

prices = [7,1,5,3,6,4]
sol = Solution()
print(sol.maxProfit(prices))
