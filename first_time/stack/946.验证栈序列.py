#
# @lc app=leetcode.cn id=946 lang=python3
#
# [946] 验证栈序列
#

# @lc code=start
# 核心问题是：在每次push操作后，我们需要判断是否进行了pop操作以及进行了多少次pop操作
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        for num in pushed:
            stack.append(num)
            while stack and  stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
        return False if stack else True
# @lc code=end

