#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start

# step down: cost[m, n] = cost[m, n-1] + [m, n-1]
# step right: cost[m, n] = cost[m-1, n] + [m-1, n]
# cost[m, n] = min(cost[m, n-1] + grid[m, n-1], cost[m-1, n] + grid[m , n-1])
from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # initialize the cost matrix
        m = len(grid)
        n = len(grid[0])
        # initialize the cost status matrix
        cost = [[0 for _ in range(n)] for _ in range(m)]
        # the first row
        for i in range(n):
            cost[0][i] = cost[0][i-1] + grid[0][i]
        # the first column
        for j in range(1, m):
            cost[j][0] = cost[j-1][0] + grid[j][0]

        for i in range(1, m):
            for j in range(1, n):
                cost[i][j] = min(cost[i][j-1] + grid[i][j], cost[i-1][j] + grid[i][j])
        return cost[-1][-1]
# @lc code=end
print(Solution().minPathSum(grid=[[1,3,1],[1,5,1],[4,2,1]]))

