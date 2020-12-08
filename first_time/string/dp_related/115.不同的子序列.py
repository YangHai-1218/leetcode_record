#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        len_s, len_t = len(s), len(t)
        dp = [[0]*(len_s+1) for _ in range(len_t+1)]
        for i in range(len_s+1):
            dp[0][i] = 1
        for i in range(1, len_t+1):
            dp[i][0] = 0
        for i in range(1, len_s+1):
            for j in range(1, len_t+1):
                if t[j-1] == s[i-1]:
                    dp[j][i] = dp[j-1][i-1] + dp[j][i-1]
                else:
                    dp[j][i] = dp[j][i-1]
        return dp[-1][-1]

# @lc code=end

sol = Solution()
print(sol.numDistinct("rabbbit", "rabbit"))
