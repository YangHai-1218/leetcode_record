#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums):
        dp = nums.copy()
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1], 0) + nums[i]
        return max(dp)

# @lc code=end

sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

