#
# @lc app=leetcode.cn id=1283 lang=python3
#
# [1283] 使结果不超过阈值的最小除数
#

# @lc code=start
import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def condition(divisor):
            return sum([math.ceil(num/divisor) for num in nums]) <= threshold
        
        left, right = 1, max(nums)
        while left < right:
            mid = left + (right - left)//2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left

# @lc code=end

