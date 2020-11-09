#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
# Doule pointer version I
# result:
#  Your runtime beats 70.29 % of python3 submissions(40ms)
#  Your memory usage beats 6.59 % of python3 submissions (13.5 MB)
# class Solution:
#     def removeElement(self, nums, val):
#         if not nums:
#             return 0
#         start_index = 0
#         for num in nums:
#             if num != val:
#                 nums[start_index] = num
#                 start_index += 1
#         return start_index

# Double pointer version II
# result:
# Your runtime beats 96.27 % of python3 submissions
# Your memory usage beats 6.09 % of python3 submissions (13.5 MB
class Solution:
    def removeElement(self, nums, val):
        if not nums:
            return 0
        start_index, end_index = 0, len(nums)-1
        while start_index <= end_index:
            if nums[start_index] == val:
                nums[start_index] =  nums[end_index]
                end_index -= 1
            else:
                start_index += 1
        return start_index
# Call library function version 
# result:
#   Your runtime beats 70.29 % of python3 submissions(40ms)
#   Your memory usage beats 5.14 % of python3 submissions (13.5 MB)
# class Solution(object):
#     def removeElement(self, nums, val):
#         for i in range(nums.count(val)):
#             nums.remove(val)
#         return len(nums)
# @lc code=end

solution = Solution()
s = solution.removeElement([4,4], 4)
print(s)