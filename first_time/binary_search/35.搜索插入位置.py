#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start

# version I
# Your runtime beats 96.97 % of python3 submissions(32ms)
# Your memory usage beats 32.48 % of python3 submissions (14 MB)
class Solution:
    def searchInsert(self, nums:list, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid 
        nums.insert(left + 1, target)
        return left


# @lc code=end

# solution = Solution()
# l = [1,3,5,6]
# print(solution.searchInsert(l, 2))
# print(l)