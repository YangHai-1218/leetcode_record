#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
# matrix
# class Solution:
#     def uniquePaths(self, m, n):
#         counts  = [[0 for i in range(m)] for j in range(n)]
#         counts[n-1] = [1 for i in range(m)]
#         for j in range(n):
#             counts[j][m-1] = 1
#         for x in range(m-2, -1, -1):
#             for y in range(n-2, -1, -1):
#                 counts[y][x] = counts[y][x+1] + counts[y+1][x]
#         return counts[0][0]

class Solution:
    def uniquePaths(self, m, n):
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0] = [1 for _ in range(n)]
        for i in range(m):
            dp[i][0] = 1 
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[-1][-1]
# @lc code=end
sol = Solution()
print(sol.uniquePaths(7,3))

