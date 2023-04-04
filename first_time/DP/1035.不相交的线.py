#
# @lc app=leetcode.cn id=1035 lang=python3
#
# [1035] 不相交的线
#

from typing import List
# @lc code=start
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0 for _ in range(len(nums2)+1)] for _ in range(len(nums1)+1)]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        return dp[-1][-1]
# @lc code=end

