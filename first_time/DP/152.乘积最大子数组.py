#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#
# [x] first time 20-12-01: read other solutions and code by yourself
# [x] second time 20-12-01: select the best solution and use cpp to implement it
# [] third time 20-12-01: after 24 hours
# [] forth time 20-12-01: after a week
# [] fifth time 20-12-01: before interview
# @lc code=start
class Solution:
    def maxProduct(self, nums):
        fmax, fmin = nums.copy(), nums.copy()
        for i in range(1, len(nums)):
            fmax[i] = max(fmax[i-1]*nums[i], fmin[i-1]*nums[i], nums[i])
            fmin[i] = min(fmax[i-1]*nums[i], fmin[i-1]*nums[i], nums[i])
        
        return max(fmax)
# @lc code=end
sol = Solution()
print(sol.maxProduct([2,-5,-2,-4,3]))
