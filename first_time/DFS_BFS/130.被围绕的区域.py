#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start
from typing import List
class Solution:
    def __init__(self) -> None:
        self.dys = [-1, 1, 0, 0]
        self.dxs = [0, 0, -1, 1]
    
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        num_rows, num_cols = len(board), len(board[0])
        connected_o = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
        board_indexs = []
        for x in range(num_cols):
            board_indexs.append((0, x))
            board_indexs.append((num_rows-1, x))
        for y in range(1, num_rows-1):
            board_indexs.append((y, 0))
            board_indexs.append((y, num_cols-1))
        for index in board_indexs:
            if board[index[0]][index[1]] == 'O':
                self._dfs(index[0], index[1], board, connected_o, num_rows, num_cols)
        
        for y in range(num_rows):
            for x in range(num_cols):
                if board[y][x] == 'O' and connected_o[y][x] == 0:
                    board[y][x] = 'X'

        


    def _dfs(self, y, x, board, connected_o, num_rows, num_cols):
        connected_o[y][x] = 1
        for dy, dx in zip(self.dys, self.dxs):
            if 0 <= y + dy < num_rows and 0 <= x+dx < num_cols:
                if board[y+dy][x+dx] == 'O' and connected_o[y+dy][x+dx] != 1:
                    connected_o[y+dy][x+dx] = 1
                    self._dfs(y+dy, x+dx, board, connected_o, num_rows, num_cols)
# @lc code=end


Solution().solve(
    [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
)
