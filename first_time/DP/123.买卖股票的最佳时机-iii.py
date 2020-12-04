#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices):
        dp = [[[0]*2 for _ in range(3)] for _ in range(len(prices))]
        for i in range(len(prices)):
            dp[i][0][0] = 0
            dp[i][0][1] = - float('inf')
        for i in range(len(prices)):
            for k in range(1, 3):
                if i == 0:
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                else:
                    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+prices[i])
                    dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]-prices[i])
        return dp[-1][-1][0]
# @lc code=end
prices = [3,3,5,0,0,3,1,4]
sol = Solution()
print(sol.maxProfit(prices))