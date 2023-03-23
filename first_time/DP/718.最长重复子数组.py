#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] 最长重复子数组
#
from typing import List
# @lc code=start
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0 for _ in range(len(nums2))] for _ in range(len(nums1))]
        ans = 0
        for i in range(len(nums2)):
            if nums1[0] == nums2[i]:
                dp[0][i] = 1
                if ans < dp[0][i]:
                    ans = dp[0][i]
        for i in range(1, len(nums1)):
            if nums2[0] == nums1[i]:
                dp[i][0] = 1
                if ans < dp[i][0]:
                    ans = dp[i][0]
        for i in range(1, len(nums1)):
            for j in range(1, len(nums2)):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                if ans < dp[i][j]:
                    ans = dp[i][j]
        return ans
            
# @lc code=end

