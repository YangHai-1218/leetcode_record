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
        counts = [1 for i in range(m)]
        for y in range(n-2, -1, -1):
            for x in range(m-1, -1, -1):
                if x == m-1:
                    counts[x] = 1
                else:
                    counts[x] = counts[x] + counts[x+1]
        return counts[0]
# @lc code=end
sol = Solution()
print(sol.uniquePaths(7,3))

