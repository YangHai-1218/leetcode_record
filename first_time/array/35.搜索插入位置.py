#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start

# version I
# Your runtime beats 96.97 % of python3 submissions(32ms)
# Your memory usage beats 32.48 % of python3 submissions (14 MB)
# class Solution:
#     def searchInsert(self, nums, target):
#         len_ = len(nums)
#         for i,num in enumerate(nums):
#             if num == target:
#                 return i
            
#             if i==0 and target < nums[i]:
#                 return 0
#             if i<len_-1:
#                 if num < target and target < nums[i+1]:
#                     return i+1
#         return len_

#version II
# Your runtime beats 96.97 % of python3 submissions(32ms)
# Your memory usage beats 32.48 % of python3 submissions (14 MB)
class Solution:
    def searchInsert(self, nums, target):
        len_ = len(nums)
        nums.append(max(target,nums[-1])+1)
        nums.insert(0,min(target,nums[0])-1)
        for i,num in enumerate(nums):
            if num == target:
                return i-1
            if num < target < nums[i+1]:
                return i
        return len_
# @lc code=end

solution = Solution()
print(solution.searchInsert([1,3,5,6], 7))