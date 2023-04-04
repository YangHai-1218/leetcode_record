#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
from typing import List
# class Solution:
#     def __init__(self) -> None:
#         self.result = 0
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         self.traversal(0, 0, nums, target)
#         return self.result

#     def traversal(self, index:int, sum_now:int, nums:List[int], target:int):
#         if sum_now == target and index == len(nums):
#             self.result += 1
#         if index == len(nums):
#             return
        
#         self.traversal(index+1, sum_now-nums[index], nums, target)
#         self.traversal(index+1, sum_now+nums[index], nums, target)

class Solution:
    def __init__(self) -> None:
        self.result = 0
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target = target + sum(nums)
        if target < 0 or target % 2 !=0 :
            return 0
        target = target // 2
        dp = [[0 for _ in range(target+1)] for _ in range(len(nums)+1)]
        dp[0][0] = 1
        for i,x in enumerate(nums):
            for c in range(target+1):
                if c < x:
                    dp[i+1][c] = dp[i][c]
                else:
                    dp[i+1][c] = dp[i][c] + dp[i][c-x]
        return dp[-1][-1]


# @lc code=end

print(Solution().findTargetSumWays([1,1,1,1,1], 3))

