#
# @lc app=leetcode.cn id=377 lang=python3
#
# [377] 组合总和 Ⅳ
#
from typing import List
# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        for i in range(0, target+1):
            for j in range(len(nums)):
                if i >= nums[j]:
                    dp[i] += dp[i-nums[j]]
        return dp[-1]
# @lc code=end

