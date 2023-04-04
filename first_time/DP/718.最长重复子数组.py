#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] 最长重复子数组
#
from typing import List
# @lc code=start
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0 for _ in range(len(nums2)+1)] for _ in range(len(nums1)+1)]
        ans = 0
        for i in range(0, len(nums1)):
            for j in range(0, len(nums2)):
                if nums1[i] == nums2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                if ans < dp[i+1][j+1]:
                    ans = dp[i+1][j+1]
        return ans
            
# @lc code=end

