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
        j=0
        for i, num in enumerate(nums):
            if num !=0 :
                nums[j] = num
                if i!=j:
                    nums[i] = 0
                j += 1

# swap 
# @lc code=end

