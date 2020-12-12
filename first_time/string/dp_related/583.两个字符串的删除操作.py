#
# @lc app=leetcode.cn id=583 lang=python3
#
# [583] 两个字符串的删除操作
#

# @lc code=start

# 最长公共子序列问题
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_1, len_2 = len(word1), len(word2)
        dp = [[0]*(len_2+1) for _ in range(len_1+1)]
        for j in range(1, len_1+1):
            for i in range(1,len_2+1):
                if word1[j-1] == word2[i-1]:
                    dp[j][i] = dp[j-1][i-1] + 1
                else:
                    dp[j][i] = max(dp[j-1][i], dp[j][i-1])
        return len_1 + len_2 - 2*dp[-1][-1]

        
# @lc code=end

