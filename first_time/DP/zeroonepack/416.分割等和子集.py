#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#
from typing import List
# @lc code=start
# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         sum_nums = sum(nums)
#         if sum_nums % 2 != 0:
#             return False
#         dp = [[0 for _ in range(sum_nums//2+1)] for _ in range(len(nums))]
#         for j in range(sum_nums//2):
#             if j >= nums[0]:
#                 dp[0][j] = nums[0]
#         for i in range(1, len(nums)):
#             for j in range(1, sum_nums//2+1):
#                 if j < nums[i]:
#                     dp[i][j] = dp[i-1][j]
#                 else:
#                     dp[i][j] = max(dp[i-1][j], dp[i-1][j-nums[i]]+nums[i])
#         if dp[-1][-1] == sum_nums // 2:
#             return True 
#         else:
#             return False

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 != 0:
            return False
        
# @lc code=end
Solution().canPartition([1,5,11,5])

