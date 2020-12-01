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
        if len(nums) <= 2:
            return max(nums)
        steal_money = [0] * (len(nums)+1)
        steal_money[1], steal_money[2] = nums[0], nums[1]
        for i in range(3, len(nums)+1):
            steal_money[i] = max(steal_money[i-2], steal_money[i-3]) + nums[i-1]
        return max(steal_money[-1], steal_money[-2])
        
# @lc code=end

sol = Solution()
print(sol.rob([2,1,1,2]))