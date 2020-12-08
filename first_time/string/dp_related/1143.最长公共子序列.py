#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        len_s, len_t = len(s), len(t)
        dp = [[0]*(len_s+1) for _ in range(len_t+1)]
        for i in range(1, len_s+1):
            for j in range(1, len_t+1):
                if t[j-1] == s[i-1]:
                    dp[j][i] = dp[j-1][i-1] + 1
                else:
                    dp[j][i] = max(dp[j][i-1], dp[j-1][i])
        return dp[-1][-1]
        
# @lc code=end
sol = Solution()
print(sol.longestCommonSubsequence("abcde", "abc"))
