#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#
from typing import List
# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 成环分为两种情况考虑
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        # 不打劫第一家，考虑打劫最后一家
        result_1 = self.robRange(nums[1:])
        # 打劫第一家，不打劫最后一家
        result_2 = self.robRange(nums[:-1])
        return max(result_1, result_2)
    
    def robRange(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)

        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]

# @lc code=end

