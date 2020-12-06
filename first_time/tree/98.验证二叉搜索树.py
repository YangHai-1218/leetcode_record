#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return False
        self.prev_node_val = float('-inf')
        return self._isvalidbst(root)

    def _isvalidbst(self, node):
        if not node:
            return True
        if not self._isvalidbst(node.left):
            return False
        
        if node.val <= self.prev_node_val:
            return False
        self.prev_node_val = node.val
        return self._isvalidbst(node.right)
        

# @lc code=end

root  = TreeNode(5)
a = TreeNode(4)
b = TreeNode(6)
c = TreeNode(3)
d = TreeNode(7)
root.left = a
root.right = b
b.left = c
b.right = d
sol = Solution()
print(sol.isValidBST(root))

