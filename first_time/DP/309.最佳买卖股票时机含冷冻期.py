#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = [[0]*2 for _ in range(len(prices))]
        for i in range(len(prices)):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
            # elif i == 1:
            #     dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i])
            #     dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            else:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
                dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i])
        return dp[-1][0]
# @lc code=end

