#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution:
    def findMin(self, nums):
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums)-1
        rotate_point = -1
        while left <= right:
            mid = int((left + right)/2)
            # this means the nums list is ordered
            if left == right == len(nums) -1 or left == right == 0:
                break
            if nums[mid] < nums[mid-1]:
                rotate_point = mid - 1
                break
            if nums[mid+1] < nums[mid]:
                rotate_point = mid
                break
            # left part is oredered, then we search the right part  
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
            # right part is ordered, then we search the left part
                right = mid - 1
        ordered_nums = nums[rotate_point+1:] + nums[:rotate_point+1] 
        return min(ordered_nums)


# @lc code=end
sol = Solution()
print(sol.findMin([11,13,15,17]))
