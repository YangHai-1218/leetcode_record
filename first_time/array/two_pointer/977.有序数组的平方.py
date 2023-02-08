#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#
from typing import List
# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        leftindex, rightindex = 0, len(nums)-1
        
        square_nums = [0 for _ in range(len(nums))]
        index = len(nums) - 1
        while leftindex <= rightindex:
            if nums[leftindex]**2 > nums[rightindex]**2:
                square_nums[index] = nums[leftindex]**2
                leftindex += 1
                index -= 1
            elif nums[leftindex]**2 < nums[rightindex]**2:
                square_nums[index] = nums[rightindex]**2
                rightindex -= 1
                index -= 1
            else:
                if leftindex == rightindex:
                    square_nums[index] = (nums[rightindex]**2)
                    index -= 1
                else:
                    square_nums[index] = nums[rightindex]**2
                    index -= 1
                    square_nums[index] = nums[leftindex]**2
                    index -= 1
                rightindex -= 1
                leftindex += 1
        return square_nums
# @lc code=end
Solution().sortedSquares([-4,-1,0,3,10])

