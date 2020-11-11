#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#
# [x] first time 20-11-10: read other solutions and code by yourself
# [x] second time 20-11-10: select the best solution and use cpp to implement it
# [x] third time 20-11-10: after 24 hours
# [] forth time 20-11-10: after a week
# [] fifth time 20-11-10: before interview
# @lc code=start
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min_stack = []


    def push(self, x):
        self.data.append(x)
        if not self.min_stack:
            self.min_stack.append(x)
        else:
            self.min_stack.append(min(x, self.min_stack[-1]))



    def pop(self):
        self.data.pop()
        self.min_stack.pop()



    def top(self):
        return self.data[-1]


    def getMin(self):
        return self.min_stack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

