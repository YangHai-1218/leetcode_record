#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def __init__(self):
        self.dxs = [1, -1, 0, 0]
        self.dys = [0, 0, 1, -1]

    def numIslands(self, grid):
        height, width = len(grid), len(grid[0])
        result = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == '1':
                    result += self.shrink(grid, i, j, height, width)
        return result

    

    def shrink(self,grid, i, j, height, width):
        stack = [(i,j)]
        while stack:
            current_y, current_x = stack.pop()
            grid[current_y][current_x] = 0
            for dy,dx in zip(self.dys, self.dxs):
                neighbor_y, neighbor_x = current_y+dy, current_x+dx
                if neighbor_y <= height-1 and neighbor_x <= width-1 and neighbor_x>=0 and neighbor_y>=0:
                    if grid[neighbor_y][neighbor_x] == '1' and (neighbor_y,neighbor_x) not in stack:
                        stack.append((neighbor_y, neighbor_x))
        return 1

                    


# @lc code=end


sol = Solution()
print(sol.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))