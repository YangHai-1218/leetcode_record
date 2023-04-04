#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_word1, len_word2 = len(word1), len(word2)
        dp = [[0] * (len_word2 + 1) for _ in range(len_word1 + 1)]
        
        for i in range(len_word1):
            for j in range(len_word2):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j]) + 1
        return dp[-1][-1]
# @lc code=end

sol = Solution()
print(sol.minDistance("horse", "ros"))