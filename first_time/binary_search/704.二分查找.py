#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#
from typing import List
# @lc code=start
class Solution:
    # def search(self, nums: List[int], target: int) -> int:
    #     left, right = 0, len(nums)-1
    #     while left <= right:
    #         mid = (left + right)//2
    #         if target < nums[mid]:
    #             right = mid - 1
    #         elif target > nums[mid]:
    #             left = mid + 1
    #         else:
    #             return mid
    #     return -1
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right)//2
            if target < nums[mid]:
                right = mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        return -1
# @lc code=end
