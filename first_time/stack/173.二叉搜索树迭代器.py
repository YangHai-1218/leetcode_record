#
# @lc app=leetcode.cn id=173 lang=python3
#
# [173] 二叉搜索树迭代器
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.stack = []
        self._inorder(self.root)
    
    def _inorder(self, node):
        if not node:
            return
        self._inorder(node.right)
        self.stack.append(node.val)
        self._inorder(node.left)


    def next(self) -> int:
        return self.stack.pop()



    def hasNext(self) -> bool:
        if not self.stack:
            return False
        else:
            return True



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

