#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n):
        self.n = n
        self.result = []
        self._generateParenthesis(0,0,'')
        return self.result

    def _generateParenthesis(self, left, right, s):
        if left == self.n and right== self.n:
            self.result.append(s)
            return
        
        if left < self.n:
            self._generateParenthesis(left+1, right, s+'(')
        if right < left:
            self._generateParenthesis(left, right+1, s+')')
        
# @lc code=end

