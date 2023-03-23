#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_word1, len_word2 = len(word1), len(word2)
        dp = [[0] * (len_word1 + 1) for _ in range(len_word2 + 1)]
        for i in range(1, len_word1+1):
            dp[0][i] = i
        for i in range(1, len_word2+1):
            dp[i][0] = i
        for j in range(1,len_word2+1):
            for i in range(1,len_word1+1):
                dp[j][i] = min(dp[j][i-1]+1, dp[j-1][i]+1, dp[j-1][i-1] + int(word1[i-1]!=word2[j-1]))
        return dp[-1][-1]
# @lc code=end

sol = Solution()
print(sol.minDistance("horse", "ros"))