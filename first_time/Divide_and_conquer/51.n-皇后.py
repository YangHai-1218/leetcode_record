#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n):
        self.n = n
        self.cols, self.pie, self.na= set(), set(), set()
        self.result = list()

        self.DFS(0,[])
        return self._generate_result()
    def DFS(self, row, cur_state):
        if row > self.n - 1:
            self.result.append(cur_state)
            return
            
        for col in range(self.n):
            if col in self.cols or row+col in self.pie or row-col in self.na:
                continue
            self.cols.add(col)
            self.pie.add(row+col)
            self.na.add(row-col)

            self.DFS(row+1, cur_state+[col])

            self.cols.remove(col)
            self.pie.remove(row+col)
            self.na.remove(row-col)
    def _generate_result(self):
        output = []
        template = ["." for _ in range(self.n)]
        for state in self.result:
            output_ = []
            for i, col in enumerate(state):
                temp = template.copy()
                temp[col] = "Q"
                temp = "".join(temp)
                output_.append(temp)
            output.append(output_)
        return output


            

# @lc code=end

