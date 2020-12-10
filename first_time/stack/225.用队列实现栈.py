#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pushqueue = []
        self.popqueue = []




    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.pushqueue.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        
        while self.pushqueue:
            self.popqueue.append(self.pushqueue.pop(0))
        return self.popqueue.pop()


    def top(self) -> int:
        """
        Get the top element.
        """
        
        while self.pushqueue:
            self.popqueue.append(self.pushqueue.pop(0))
        return self.popqueue[-1]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if not self.popqueue and not self.pushqueue:
            return True
        else:
            return False



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end
obj = MyStack()
obj.push(1)
obj.push(2)
obj.top()
obj.pop()
obj.empty()

