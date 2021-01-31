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
    def searchInsert(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left)//2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left


# @lc code=end

solution = Solution()
print(solution.searchInsert([1,3,5,6], 7))