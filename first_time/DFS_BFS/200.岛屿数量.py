#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start

# DFS version
# class Solution:
#     def __init__(self):
#         self.dxs = [1, -1, 0, 0]
#         self.dys = [0, 0, 1, -1]

#     def numIslands(self, grid):
#         height, width = len(grid), len(grid[0])
#         result = 0
#         for i in range(height):
#             for j in range(width):
#                 if grid[i][j] == '1':
#                     result += self.shrink(grid, i, j, height, width)
#         return result

    

#     def shrink(self,grid, i, j, height, width):
#         stack = [(i,j)]
#         while stack:
#             current_y, current_x = stack.pop()
#             grid[current_y][current_x] = 0
#             for dy,dx in zip(self.dys, self.dxs):
#                 neighbor_y, neighbor_x = current_y+dy, current_x+dx
#                 if neighbor_y <= height-1 and neighbor_x <= width-1 and neighbor_x>=0 and neighbor_y>=0:
#                     if grid[neighbor_y][neighbor_x] == '1' and (neighbor_y,neighbor_x) not in stack:
#                         stack.append((neighbor_y, neighbor_x))
#         return 1


# BFS version
# class Solution:
#     def __init__(self):
#         self.dxs = [1, -1, 0, 0]
#         self.dys = [0, 0, 1, -1]

#     def numIslands(self, grid):
#         M, N = len(grid), len(grid[0])
#         if M == 0 or N == 0:
#             return 0
#         ans = 0
#         for j in range(M):
#             for i in range(N):
#                 if grid[j][i] == "1":
#                     grid[j][i] = "0"
#                     ans += 1
#                     queue = [(j,i)]
#                     while queue:
#                         y, x = queue.pop(0)
#                         for dy, dx in zip(self.dys, self.dxs):
#                             if 0 <= y+dy < M and 0 <= x+dx < N:
#                                 if grid[y+dy][x+dx] == "1":
#                                     grid[y+dy][x+dx] = "0"
#                                     queue.append((y+dy,x+dx))
#         return ans

# DFS stack version
# class Solution:
#     def __init__(self):
#         self.dxs = [1, -1, 0, 0]
#         self.dys = [0, 0, 1, -1]
#     def numIslands(self, grid):
#         M, N = len(grid), len(grid[0])
#         if M == 0 or N == 0:
#             return 0
#         ans = 0
#         for j in range(M):
#             for i in range(N):
#                 if grid[j][i] == "1":
#                     ans += 1
#                     grid[j][i] = "0"
#                     stack = [(j,i)]
#                     while stack:
#                         y, x = stack.pop()
#                         for dy, dx in zip(self.dys, self.dxs):
#                             if 0 <= y+dy < M and 0 <= x+dx < N:
#                                 if grid[y+dy][x+dx] == '1':
#                                     grid[y+dy][x+dx] = '0'
#                                     stack.append((y+dy, x+dx))
#         return ans


# DFS reursion version
class Solution:
    def __init__(self):
        self.dxs = [1, -1, 0, 0]
        self.dys = [0, 0, 1, -1]
    def numIslands(self, grid):
        self.M, self.N = len(grid), len(grid[0])
        if self.M == 0 or self.N == 0:
            return 0
        ans = 0
        for j in range(self.M):
            for i in range(self.N):
                if grid[j][i] == '1':
                    ans += 1
                    grid[j][i] = "0"
                    self._dfs(grid, i, j)
        return ans
    
    def _dfs(self, grid, x, y):
        for dy, dx in zip(self.dys, self.dxs):
            if 0 <= y+dy < self.M and 0 <= x+dx < self.N:
                if grid[y+dy][x+dx] == '1':
                    grid[y+dy][x+dx] = '0'
                    self._dfs(grid, x+dx, y+dy)

# @lc code=end


sol = Solution()
print(sol.numIslands([["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))