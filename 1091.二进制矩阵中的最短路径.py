#
# @lc app=leetcode.cn id=1091 lang=python3
#
# [1091] 二进制矩阵中的最短路径
#

# @lc code=start
class Solution:
    def shortestPathBinaryMatrix(self, grid):
        if grid[0][0] == 1:
            return -1
        visited = []
        node = (0,0)
        self.N = len(grid)
        self.dx = [1,0,-1,0,1,-1,1,-1]
        self.dy = [0,1,0,-1,1,-1,-1,1]
        self.result = []


        return min(self.result) if self.result else -1

    def _shortestPathBinaryMatrix(self, grid, visited, node, length):

        if node == (self.N-1, self.N-1):
            self.result.append(length+1)
            return 
        
        visited.append(node)
        x, y = node[0], node[1]
        for dx, dy in zip(self.dx, self.dy):
            if 0 <= x+dx < self.N and 0 <= y+dy < self.N and (x+dx,y+dy) not in visited:
               if grid[y+dy][x+dx] != 1:
                   self._shortestPathBinaryMatrix(grid, visited, (x+dx,y+dy), length+1)
        visited.remove(node)
       
            


        
# @lc code=end

sol = Solution()
result = sol.shortestPathBinaryMatrix([[0,0,1,1,0,0],[0,0,0,0,1,1],[1,0,1,1,0,0],[0,0,1,1,0,0],[0,0,0,0,0,0],[0,0,1,0,0,0]])
print(result)