#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#
# [x] first time 20-12-01: read other solutions and code by yourself
# [x] second time 20-12-01: select the best solution and use cpp to implement it
# [] third time 20-12-01: after 24 hours
# [] forth time 20-12-01: after a week
# [] fifth time 20-12-01: before interview
# @lc code=start
class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]
        
# @lc code=end

sol = Solution()
print(sol.rob([2,1,1,2]))