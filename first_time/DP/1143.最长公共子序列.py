#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#
# [x] first time 20-12-01: read other solutions and code by yourself
# [x] second time 20-12-01: select the best solution and use cpp to implement it
# [] third time 20-12-01: after 24 hours
# [] forth time 20-12-01: after a week
# [] fifth time 20-12-01: before interview
# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1, text2):
        m, n= len(text1), len(text2)
        if m==0 and n==0:
            return 0
        counts = [[0]*(n+1) for i in range(m+1)]
        for y in range(1,m+1):
            for x in range(1,n+1):
                if text1[y-1] == text2[x-1]:
                    counts[y][x] = counts[y-1][x-1] + 1
                else:
                    counts[y][x] = max(counts[y-1][x], counts[y][x-1])
        return counts[-1][-1]

# 公共子串
class Solution:
    def longestCommonSubsequence(self, text1, text2):
        m, n= len(text1), len(text2)
        if m==0 and n==0:
            return 0
        counts = [[0]*(n+1) for i in range(m+1)]
        for y in range(1,m+1):
            for x in range(1,n+1):
                if text1[y-1] == text2[x-1]:
                    counts[y][x] = counts[y-1][x-1] + 1
                else:
                    counts[y][x] = 0
        return max(counts)
# @lc code=end

