#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#
# [x] first time 20-12-03: read other solutions and code by yourself
# [x] second time 20-12-03: select the best solution and use cpp to implement it
# [] third time 20-12-03: after 24 hours
# [] forth time 20-12-03: after a week
# [] fifth time 20-12-03: before interview
# @lc code=start
class Solution:
    def isValidSudoku(self, board):
        self.cols = [{i+1:0 for i in range(9)} for _ in range(9)]
        self.boxs = [{i+1:0 for i in range(9)} for _ in range(9)]
        for y in range(9):
            self.rows = {i+1:0 for i in range(9)}
            for x in range(9):
                if board[y][x] != ".":
                    number = int(board[y][x])
                    self.cols[x][number] += 1
                    self.rows[number] += 1
                    box_index = (y//3)*3 + x//3
                    self.boxs[box_index][number] += 1
                    if self.cols[x][number] > 1 or self.boxs[box_index][number] > 1 \
                        or self.rows[number] > 1:
                        return False
        return True
# @lc code=end

board = [[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
sol = Solution()
result = sol.isValidSudoku(board)
print(result)