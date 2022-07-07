#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#

# @lc code=start
class Solution:
    def __init__(self):
        self.dx = [-1, 0, 1, 0]
        self.dy = [0, -1, 0, 1]
    def maxAreaOfIsland(self, grid) -> int:
        self.h, self.w = len(grid), len(grid[0])
        ans = 0
        self.grid = grid
        for y in range(self.h):
            for x in range(self.w):
                if self.grid[y][x] == 1:
                    ans = max(ans, self._dfs(y, x))
        return ans
    def _dfs(self, y, x):
        if y < 0 or y >= self.h or x <0  or x>= self.w or self.grid[y][x] == 0:
            return 0
        
        self.grid[y][x] = 0
        up = self._dfs(y-1, x)
        left = self._dfs(y, x-1)
        down = self._dfs(y+1, x)
        right = self._dfs(y, x+1)
        return up + left + down + right + 1


        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    ans = solution.maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]])
    print(ans)

