#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums, target):
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        rotate_point = -1
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                rotate_point = i
                break
        if nums[0] <= target <= nums[rotate_point]:
            base_index = 0
            nums = nums[0:rotate_point+1]
        elif nums[rotate_point+1] <= target <= nums[-1]:
            base_index = rotate_point
            nums = nums[rotate_point:-1]
        else:
            return -1
        left, right = 0, len(nums)-1
        while left <= right:
            mid = int((left+right)/2)
            if nums[mid] == target:
                return base_index + mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1 

# class Solution:
#     def search(self, nums, target):
#         left, right = 0, len(nums)-1
#         while left <= right:
#             mid = int((left+right)/2)
#             if nums[mid] == target:
#                 return mid
#             # left part is ordered
#             elif nums[left] <= nums[mid]:
#                 if nums[left] <= target < nums[mid]:
#                     right = mid - 1
#                 else:
#                     left = mid + 1
#             else:
#             # right part is ordered
#                 if nums[mid] < target <= nums[right]:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#         return -1
# @lc code=end

sol = Solution()
print(sol.search([4,5,6,7,0,1,2], 0))

