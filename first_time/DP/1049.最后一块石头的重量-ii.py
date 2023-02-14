#
# @lc app=leetcode.cn id=1049 lang=python3
#
# [1049] 最后一块石头的重量 II
#
from typing import List
# @lc code=start
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sum_stones = sum(stones)
        flag = sum_stones // 2
        dp = [0 for _ in range(flag+1)]
        for i in range(0, len(stones)):
            for j in range(flag, -1, -1):
                if j < stones[i]:
                    continue
                dp[j] = max(dp[j], dp[j-stones[i]]+stones[i])
        return sum_stones - dp[flag] - dp[flag]
# @lc code=end

