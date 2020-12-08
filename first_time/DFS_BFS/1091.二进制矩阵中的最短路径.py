#
# @lc app=leetcode.cn id=1091 lang=python3
#
# [1091] 二进制矩阵中的最短路径
#

# @lc code=start
class Solution:
    def shortestPathBinaryMatrix(self, grid):
        if grid[0][0] == 1 or grid[-1][-1]==1:
            return -1
        self.N = len(grid)
        
        self.dx = [1,0,-1,0,1,-1,1,-1]
        self.dy = [0,1,0,-1,1,-1,-1,1]
        queue = [(0,0)]
        grid[0][0] = 1
        result = -1
        while queue:
            current_level_size = len(queue)
            result += 1
            for _ in range(current_level_size):
                y, x = queue.pop(0)                
                if y == self.N - 1 and x == self.N - 1:
                    return result+1
                for dx, dy in zip(self.dx, self.dy):
                    if 0 <= x+dx < self.N and 0 <= y+dy < self.N:
                        if grid[y+dy][x+dx] != 1:
                            queue.append((y+dy, x+dx))
                            grid[y+dy][x+dx] =  1

        return -1
            


        
# @lc code=end

sol = Solution()
result = sol.shortestPathBinaryMatrix([[0,1],[1,0]])
print(result)