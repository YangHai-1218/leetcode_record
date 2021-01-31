#
# @lc app=leetcode.cn id=334 lang=python3
#
# [334] 递增的三元子序列
#

# @lc code=start
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min_num, mid_num = 10000000000000, 10000000000000
        for num in nums:
            if num <= min_num:
                min_num = num
            elif num <= mid_num:
                mid_num = num
            elif num > mid_num:
                return True
        return False
# @lc code=end

