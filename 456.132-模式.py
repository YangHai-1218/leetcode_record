#
# @lc app=leetcode.cn id=456 lang=python3
#
# [456] 132模式
#

# @lc code=start
class Solution:
    def find132pattern(self, nums):
        if len(nums) < 3:
            return False
        
        stack = [nums[0], nums[1]]
        nums_ = [False] * len(nums)
        if nums[1] > nums[0]:
            nums_[1] = True
        for i in range(2, len(nums)):
            if nums[i] < stack[-1]:
                if nums_[i-1]  
            while stack and nums[i] >= stack[-1]:
                nums_[i] = True
                stack.pop()
            
            if nums_[i] == True:
                return True
        return False

# @lc code=end
sol = Solution()
print(sol.find132pattern([3, 1, 4, 2]))
