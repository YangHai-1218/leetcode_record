#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#
from typing import List
# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left_index, right_index = 0, 0
        result = 10000000
        sub_sum = 0
        while right_index < len(nums):
            sub_sum += nums[right_index]
            while sub_sum >= target:
                sub_len = right_index - left_index + 1
                result = sub_len if sub_len < result else result
                sub_sum -= nums[left_index]
                left_index += 1
            right_index += 1
        return result if result != 10000000 else 0
# @lc code=end

