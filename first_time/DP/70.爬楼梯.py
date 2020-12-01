#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
# dp version
class Solution:
    def climbStairs(self, n):
        if n <= 2:
            return n
        nums = [0 for i in range(n)]
        nums[0] = 1
        nums[1] = 2
        for i in range(2, n):
            nums[i] = nums[i-1] + nums[i-2]
        return nums[n-1]

# @lc code=end

