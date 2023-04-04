#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start
from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pushqueue = deque()
        self.popqueue = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.pushqueue.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.empty():
            return None
    
        for i in range(len(self.pushqueue)-1):
            self.popqueue.append(self.pushqueue.popleft())
        self.pushqueue, self.popqueue = self.popqueue, self.pushqueue
        return self.popqueue.popleft()


    def top(self) -> int:
        """
        Get the top element.
        """
        if self.empty():
            return None
    
        return self.pushqueue[-1]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if not self.pushqueue:
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

