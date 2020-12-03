#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
# class Solution:
#     def solveSudoku(self, board):
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         for y in range(9):
#             for x in range(9):
#                 if board[y][x] != '.':
#                     continue
#                 for char in '123456789':
#                     board[y][x] = char
#                     if self.check_valid(board):
#                         if self.solveSudoku(board):
#                             return True
#                         board[y][x] = '.'
#                     else:
#                         board[y][x] = '.'
#                 # if all '123456789' can't solve problem, then pass this solution
#                 return False
        
#         return True

#     def check_valid(self, board):
#         cols = [{i+1:0 for i in range(9)} for _ in range(9)]
#         boxs = [{i+1:0 for i in range(9)} for _ in range(9)]
#         for y in range(9):
#             rows = {i+1:0 for i in range(9)}
#             for x in range(9):
#                 if board[y][x] != ".":
#                     number = int(board[y][x])
#                     cols[x][number] += 1
#                     rows[number] += 1
#                     box_index = (y//3)*3 + x//3
#                     boxs[box_index][number] += 1
#                     if cols[x][number] > 1 or boxs[box_index][number] > 1 \
#                         or rows[number] > 1:
#                         return False
#         return True


class Solution:
    def solveSudoku(self, board):
        self.rows = [set(range(1,10)) for _ in range(9)]
        self.cols = [set(range(1,10)) for _ in range(9)]
        self.boxs = [set(range(1,10)) for _ in range(9)]
        empty = []
        for y in range(9):
            for x in range(9):
                if board[y][x] != '.':
                    number = int(board[y][x])
                    self.rows[y].remove(number)
                    self.cols[x].remove(number)
                    self.boxs[(y//3)*3+x//3].remove(number)
                else:
                    empty.append((x,y))
        self._backtrack(empty, board)

    
    def _backtrack(self, empty, board):
        if len(empty) ==0:
            return True
        x, y = empty.pop(0)
        for val in self.rows[y] & self.cols[x] & self.boxs[(y//3)*3+x//3]:
            self.rows[y].remove(val)
            self.cols[x].remove(val)
            self.boxs[(y//3)*3+x//3].remove(val)
            if self._backtrack(empty, board):
                board[y][x] = str(val)
                return True
            self.rows[y].add(val)
            self.cols[x].add(val)
            self.boxs[(y//3)*3+x//3].add(val)
        empty.insert(0,(x,y))
        return False


        


# @lc code=end

board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
sol = Solution()
sol.solveSudoku(board)
print(board)