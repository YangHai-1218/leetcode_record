#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = int((left+right)/2)
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left_, right_ = mid-1 , mid+1
                while left_ >= 0 and nums[left_] == target:
                    left_ -= 1
                while right_ <= len(nums) -1 and nums[right_] == target:
                    right_ += 1
                return [left_+1 , right_-1]
        return [-1,-1]


# @lc code=end
sol = Solution()
print(sol.searchRange([1],1))
