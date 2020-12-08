#
# @lc app=leetcode.cn id=892 lang=python3
#
# [892] 三维形体的表面积
#

# @lc code=start
# 思路：
# 1. 先计算所有立方体没有没有被遮住的话，总的表面积
# 2. 计算被遮盖的面的数量
    # - 同一行前一列，遮盖的面的数量等于最小高度
    # - 同一列前一行，遮盖的面的数量等于最小高度
# 3. 总的表面积 - 被遮盖的面的数量*2
class Solution:
    def surfaceArea(self, grid):
        res = sum([sum(i) for i in grid]) * 6
        cover = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] > 1:
                    cover += grid[i][j] - 1
                # 同一列 前一行
                if i > 0:
                    cover += min(grid[i-1][j], grid[i][j])
                # 同一行 前一列
                if j > 0:
                    cover += min(grid[i][j-1], grid[i][j])
        return res - cover * 2

        
# @lc code=end

grid = [[1,0],[0,2]]

sol = Solution()
print(sol.surfaceArea(grid))
