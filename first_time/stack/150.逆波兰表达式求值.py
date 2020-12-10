#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start
import math
class Solution:
    def evalRPN(self, tokens):

        set_op = set('+-*/')
        stack_op = []
        stack_num = []
        for obj in tokens:
            if obj in set_op:
                num_1 = stack_num.pop()
                num_2 = stack_num.pop()
                num = int(math.modf(eval(num_2+obj+num_1))[-1])
                stack_num.append(str(num))
            else:
                stack_num.append(obj)
        return int(stack_num[-1])

# @lc code=end

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
sol = Solution()
print(sol.evalRPN(tokens))