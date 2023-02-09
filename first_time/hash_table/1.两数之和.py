#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
# class Solution:
#     def twoSum(self, nums, target):
#         temp = {}
#         for i, num in enumerate(nums):
#             if target - num in temp:
#                 return [temp[target-num], i]
#             temp[num] = i
#         return None
class Solution:
    def twoSum(self, nums, target):
        temp = {}
        for i, num in enumerate(nums):
            if target - num in temp:
                return [temp[target-num], i]
            temp[num] = i
        return None
# @lc code=end

