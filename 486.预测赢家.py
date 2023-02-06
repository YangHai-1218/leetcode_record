#
# @lc app=leetcode.cn id=486 lang=python3
#
# [486] 预测赢家
#

# @lc code=start
# Refer to the official solution: https://leetcode.cn/problems/predict-the-winner/solution/yu-ce-ying-jia-by-leetcode-solution
# Notes:
# let dp[i, j] be the maximum score difference between the "current" player and the other player
# The dp formula is dp[i, j] = max(nums[i] - dp[i+1, j], nums[j] - dp[i, j-1])
# let say for dp[i,j], it represents the maximum score difference between player a and player b
# then dp[i-1, j] represents the maximum score difference between player b and player a. 
# In other words, for dp[i-1, j], player b got dp[i-1, j] score, while player a got zero score.
# It equals to that player b got zero score, while player a got -dp[i-1, j] score.
# So when checking the dp[0, -1], we get the maximum score which can be earned by the current plater, "first-hand player"

from typing import List
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        elem_num = len(nums)
        dp = [[0 for _ in range(elem_num)] for _ in range(elem_num)]
        for i in range(elem_num):
            dp[i][i] = nums[i]
        for i in range(elem_num-1, -1, -1):
            for j in range(i, elem_num):
                if i >= j:
                    continue
                dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
        return dp[0][-1] >= 0


# @lc code=end
print(Solution().PredictTheWinner([1,5,2]))
