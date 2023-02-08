#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#
# Tag: array   two-pointers
# [x] first time 20-11-09: read other solutions,
# [] second time 20-11-09: code by yourserlf
# [] third time 20-11-09: after 24 hours
# [] forth time 20-11-09: after a week
# [] fifth time 20-11-09: before interview
# @lc code=start


# two pointers version
class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        slow_pointer, fast_pointer = 0,0 
        while fast_pointer < n:
            if nums[fast_pointer] != 0:
                nums[slow_pointer] = nums[fast_pointer]
                slow_pointer += 1
            fast_pointer += 1
        if slow_pointer < n:
            nums[slow_pointer:] = [0 for _ in range(n - slow_pointer)]
    
            


# swap 
# @lc code=end

