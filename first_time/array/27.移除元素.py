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
class Solution:
    def removeElement(self, nums, val):
        if not nums:
            return 0
        fast_pointer, slow_pointer = 0, 0
        while fast_pointer < len(nums):
            if (nums[fast_pointer] != val):
                nums[slow_pointer] = nums[fast_pointer]
                slow_pointer += 1
            fast_pointer += 1
        return slow_pointer

# Double pointer version II
# class Solution:
#     def removeElement(self, nums, val):
#         if not nums:
#             return 0
#         start_index, end_index = 0, len(nums)-1
#         while start_index <= end_index:
#             if nums[start_index] == val:
#                 nums[start_index] =  nums[end_index]
#                 end_index -= 1
#             else:
#                 start_index += 1
#         return start_index
# @lc code=end

solution = Solution()
s = solution.removeElement([4,4], 4)
print(s)